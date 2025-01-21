import warnings
from flask import Flask, request, render_template
import pandas as pd
from recbole.quick_start import load_data_and_model
import torch
import warnings

# 忽略两种 Warning
warnings.simplefilter(action='ignore', category=(FutureWarning, UserWarning))

model_path = '../saved/SpectralCF-Jan-17-2025_21-36-08.pth'

# 加载数据和模型
config, model, dataset, train_data, valid_data, test_data = load_data_and_model(
    model_file=model_path
)

# 读取课程信息CSV文件
course_df = pd.read_csv('dataset/courses_info.csv')


def get_course_info(course_code):
    """根据课程代码查找课程详细信息"""
    row = course_df[course_df['Course Code'] == course_code]
    if not row.empty:
        return row.iloc[0].to_dict()
    else:
        return None


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = request.form['user_id']
    k = int(request.form['topk']) + 1

    # 将用户ID转换为内部ID
    uid_series = dataset.token2id(dataset.uid_field, [user_id])

    device = model.device
    scores = model.full_sort_predict({'u_id': torch.tensor(uid_series).to(device)}).view(1, -1)
    topk_score, topk_iid_list = scores.topk(k, dim=1)
    external_item_list = dataset.id2token(dataset.iid_field, topk_iid_list.cpu())

    recommended_courses = []
    for item_code in external_item_list[0]:
        if item_code != '[PAD]':
            course_info = get_course_info(item_code)
            if course_info:
                recommended_courses.append(course_info)

    return render_template('recommendation.html', courses=recommended_courses)


if __name__ == '__main__':
    app.run(debug=True)
