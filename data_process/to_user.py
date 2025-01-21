import pandas as pd

# 从数据表格转换 recbole 需要的 user 类型原子文件

input_csv_path = 'hmx_int_id.csv'
output_path = 'hmx-400k.user'


def convert_to_user(input_csv_path, output_user_path):
    # 读取csv文件
    df = pd.read_csv(input_csv_path)

    # 选取需要的列，并重命名以匹配RecBole格式
    df_selected = df[['u_id', 'gender', 'age', 'education']].copy()

    # 去重，只保留重复出现的第一个user_id对应的行
    df_unique_users = df_selected.drop_duplicates(subset='u_id', keep='first')

    # 写入到.user文件，指定编码为utf-8
    with open(output_user_path, 'w', encoding='utf-8') as file:
        # 写入头信息
        file.write('u_id:token\tgender:token\tage:token\teducation:token\n')
        for index, row in df_unique_users.iterrows():
            line = f"{row['u_id']}\t{row['gender']}\t{int(row['age'])}\t{row['education']}\n"
            file.write(line)

    print(f"转换完成，新文件已保存为 {output_user_path}")


convert_to_user(input_csv_path, output_path)