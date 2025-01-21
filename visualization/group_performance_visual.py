import pandas as pd
import matplotlib.pyplot as plt

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

colors = ['#465E70', '#2C7FB8', '#91BD61', '#D9A54C']

metrics = ['MRR', 'NDCG', 'Recall', 'Precision']

for metric in metrics:
    fig, ax = plt.subplots(figsize=(12, 8))

    # 绘制条形图
    bar_positions = range(len(df['模型']))
    width = 0.8  # 条形宽度
    for i, (model, value) in enumerate(zip(df['模型'], df[metric])):
        color = colors[i // 2 % len(colors)]  # 每两个算法使用相同的颜色
        ax.bar(bar_positions[i], value, width, label=model, color=color)

        # 在每个条形上方添加数值标签
        ax.annotate(f"{value:.4f}",
                    xy=(bar_positions[i], value),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=9)

    # 设置标题和标签
    ax.set_title(f'{metric} 对比', fontsize=14, fontweight='bold')
    ax.set_xlabel('模型算法', fontsize=12)
    ax.set_ylabel(metric, fontsize=12)

    # 自动调整x轴标签角度以提高可读性
    plt.xticks(bar_positions, df['模型'], rotation=45, ha='right', fontsize=10)

    # 添加网格线
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)

    # 紧凑布局
    plt.tight_layout()

    # 保存图片
    plt.savefig(f'{metric}_comparison.png', dpi=300, bbox_inches='tight')

    # 显示图表
    plt.show()
