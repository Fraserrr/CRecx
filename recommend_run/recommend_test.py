import warnings
import pandas as pd
from recbole.quick_start import load_data_and_model
import torch

# 可调用各个模型，测试模型推理功能

# 忽略两种 Warning
warnings.simplefilter(action='ignore', category=(FutureWarning, UserWarning))

model_paths = {
    'bpr': 'saved/BPR-Jan-17-2025_14-56-15.pth',
    'neumf': 'saved/NeuMF-Jan-17-2025_16-00-56.pth',
    'dmf': 'saved/DMF-Jan-17-2025_16-58-02.pth',
    'knn': 'saved/ItemKNN-Jan-17-2025_18-33-16.pth',
    'spect': '../saved/SpectralCF-Jan-17-2025_21-36-08.pth',
    'lightgcn': 'saved/LightGCN-Jan-17-2025_21-58-07.pth',
    'fism': 'saved/FISM-Jan-17-2025_20-24-13.pth',
    'nais': 'saved/NAIS-Jan-17-2025_20-54-01.pth'
}

# 选择当前使用的模型
current_model = 'spect'

# 定义测试的 uid 和 topk
test_user_ids = ['49']
k = 8

print("\nLoading the model...\nIt may take a few dozen seconds...")

# 加载数据和模型
config, model, dataset, train_data, valid_data, test_data = load_data_and_model(
    model_file=model_paths[current_model],
)

print("Calling the model to recommend courses for you...")

# 获取模型所在的设备
device = model.device

# 将用户ID转换为内部ID
uid_series = dataset.token2id(dataset.uid_field, test_user_ids)

# 确保输入张量在正确的设备上
scores = model.full_sort_predict({'u_id': torch.tensor(uid_series).to(device)}).view(len(test_user_ids), -1)

# 由于 topk 操作不会改变张量的设备位置，这里不需要特别处理
topk_score, topk_iid_list = scores.topk(k, dim=1)
external_item_list = dataset.id2token(dataset.iid_field, topk_iid_list.cpu())

# 读取课程信息CSV文件
course_df = pd.read_csv('dataset/courses_info.csv')


def get_course_info(course_code):
    """根据课程代码查找课程详细信息"""
    row = course_df[course_df['Course Code'] == course_code]
    if not row.empty:
        return row.iloc[0].to_dict()
    else:
        return None


print(f"\nTop-{k} Scores for user {test_user_ids}:")
print(topk_score)

print(f"\nTop-{k} Item IDs for user {test_user_ids}:")
print(topk_iid_list)

print(f"\nHello user {test_user_ids}! Here are top-{k-1} courses recommended for you :\n")
for idx, item_code in enumerate(external_item_list[0]):
    if item_code != '[PAD]':
        course_info = get_course_info(item_code)
        if course_info:
            print(f"Rank {idx}: {item_code}")
            print(f"  Institution: {course_info['Institution']}")
            print(f"  Title: {course_info['Full Title']}")
            print(f"  Description: {course_info['Description']}")
            print(f"  Resource: {course_info['Resource Link']}")
