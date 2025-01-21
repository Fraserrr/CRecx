import pandas as pd
from datetime import datetime

# 从清洗好的数据表格中，提取出需要的字段，并进一步处理

# 定义输入和输出文件路径
input_file = 'hmx_eda.csv'
output_file = 'hmx_selected.csv'

# 定义需要提取的字段
fields_to_extract = [
    'user_id',
    'gender',
    'age',
    'education',
    'course_code',
    'certified',
    'grade',
    'time_registered',
    'nchapters'
]

# 补充每个课程代码对应的总章节数
total_chapters_by_course = {
    'CB22x': 27,
    'CS50x': 12,
    'ER22x': 34,
    'PH207x': 16,
    'PH278x': 11,
    '14.73x': 12,
    '2.01x': 13,
    '3.091x': 16,
    '6.002x': 18,
    '6.00x': 19,
    '7.00x': 18,
    '8.02x': 21,
    '8.MReV': 47,
}

# 读取原始CSV文件
df = pd.read_csv(input_file)

# 检查并提取所需的字段
if all(field in df.columns for field in fields_to_extract):
    df_extracted = df[fields_to_extract].copy()  # 显式地复制DataFrame

    # time_registered 格式为 'YYYY-MM-DD'
    def convert_to_timestamp(date_str):
        try:
            dt = datetime.strptime(date_str, '%Y-%m-%d')
            return int(dt.timestamp())
        except ValueError:
            return None

    # 将 time_registered 转换为 Unix 时间戳
    df_extracted['time_registered'] = df_extracted['time_registered'].apply(convert_to_timestamp)

    # 计算 nchapters 占总章节数的百分比，并创建 rating 列
    def calculate_rating(row):
        course_code = row['course_code']
        nchapters = row['nchapters']
        total_chapters = total_chapters_by_course.get(course_code)

        if total_chapters is not None and nchapters is not None:
            percentage = (nchapters / total_chapters) * 100
            return int(percentage)  # 保留整数
        else:
            return None

    # 应用 calculate_rating 函数并创建 rating 列
    df_extracted['rating'] = df_extracted.apply(calculate_rating, axis=1)

    # 保存提取后的数据到新的CSV文件
    df_extracted.to_csv(output_file, index=False)
    print(f"提取完成，新文件已保存为 {output_file}")
else:
    missing_fields = [field for field in fields_to_extract if field not in df.columns]
    print(f"以下字段在原始数据集中不存在: {missing_fields}")
