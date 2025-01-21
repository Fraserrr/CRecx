import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# 创建数据框
data = {
    '模型': ['ItemKNN', 'NAIS', 'BPR', 'FISM', 'NeuMF', 'DMF', 'SpectralCF', 'LightGCN'],
    'MRR': [0.3403, 0.4918, 0.3397, 0.5096, 0.5098, 0.2765, 0.5102, 0.4703],
    'NDCG': [0.4565, 0.5587, 0.4177, 0.5796, 0.5804, 0.3834, 0.5805, 0.5544],
    'Recall': [0.8129, 0.7679, 0.6599, 0.8005, 0.803, 0.7168, 0.8008, 0.8089],
    'Precision': [0.1355, 0.128, 0.11, 0.1334, 0.1338, 0.1195, 0.1335, 0.1348]
}
df = pd.DataFrame(data)

# 设置中文字体路径
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

colors = ['#004c6d', '#69b0c1', '#00717a', '#a0d8e2']

metrics = ['MRR', 'NDCG', 'Recall', 'Precision']
models = df['模型'].values
n_models = len(models)
bar_width = 0.2  # 条形宽度
index = range(n_models)  # 每个算法的位置

fig, ax = plt.subplots(figsize=(16, 10))

# 绘制分组条形图
for i, metric in enumerate(metrics):
    positions = [x + bar_width * i for x in index]
    ax.bar(positions, df[metric], bar_width, label=metric, color=colors[i])

    # 在每个条形上方添加数值标签
    for j, value in enumerate(df[metric]):
        ax.annotate(f"{value:.4f}",
                    xy=(positions[j], value),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=9)

# 设置标题和标签
ax.set_title('模型算法性能对比', fontsize=16, fontweight='bold')
ax.set_xlabel('模型算法', fontsize=14)
ax.set_ylabel('评测指标值', fontsize=14)

# 自动调整x轴标签角度以提高可读性
plt.xticks([r + bar_width * 1.5 for r in range(n_models)], models, rotation=45, ha='right', fontsize=10)

# 添加图例
ax.legend(title='评测指标', bbox_to_anchor=(1.01, 1), loc='upper left')

# 添加网格线
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# 紧凑布局
plt.tight_layout()

# 保存图片
plt.savefig('original_performance.png', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()

# 归一化处理
scaler = MinMaxScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df.drop('模型', axis=1)), columns=df.columns[1:], index=df.index)
df_normalized['模型'] = df['模型']

colors = ['#004c6d', '#69b0c1', '#00717a', '#a0d8e2']
metrics = ['MRR', 'NDCG', 'Recall', 'Precision']
models = df_normalized['模型'].values
n_models = len(models)
bar_width = 0.2  # 条形宽度
index = range(n_models)  # 每个算法的位置

fig, ax = plt.subplots(figsize=(16, 10))

# 绘制分组条形图
for i, metric in enumerate(metrics):
    positions = [x + bar_width * i for x in index]
    values = df_normalized[metric].values
    ax.bar(positions, values, bar_width, label=metric, color=colors[i])

    # 在每个条形上方添加数值标签
    for j, value in enumerate(values):
        ax.annotate(f"{value:.3f}",
                    xy=(positions[j], value),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=9)

# 设置标题和标签
ax.set_title('各算法性能对比（归一化后）', fontsize=16, fontweight='bold')
ax.set_xlabel('模型算法', fontsize=14)
ax.set_ylabel('评测指标归一化值', fontsize=14)

# 自动调整x轴标签角度以提高可读性
plt.xticks([r + bar_width * 1.5 for r in range(n_models)], models, rotation=45, ha='right', fontsize=10)

# 添加图例
ax.legend(title='评测指标', bbox_to_anchor=(1.01, 1), loc='upper left')

# 添加网格线
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# 紧凑布局
plt.tight_layout()

# 保存图片
plt.savefig('total_performance.png', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()
