import pandas as pd

# 从数据表格转换 recbole 需要的 inter 类型原子文件

input_csv_path = 'hmx_int_id.csv'
output_path = 'hmx-400k.inter'


def convert_to_inter(input_csv_path, output_inter_path):
    # 读取csv文件
    df = pd.read_csv(input_csv_path)

    # 选取需要的列
    df_selected = df[['u_id', 'course_code', 'rating', 'time_registered']].copy()

    # 格式化数据为RecBole接受的格式
    df_inter = df_selected[['u_id', 'course_code', 'rating', 'time_registered']]

    # 写入到.inter文件，指定编码为utf-8
    with open(output_inter_path, 'w', encoding='utf-8') as file:
        file.write('u_id:token\tcourse_code:token\trating:float\ttime_registered:float\n')
        for index, row in df_inter.iterrows():
            line = f"{row['u_id']}\t{row['course_code']}\t{row['rating']}\t{row['time_registered']}\n"
            file.write(line)

    print(f"转换完成，新文件已保存为 {output_inter_path}")


convert_to_inter(input_csv_path, output_path)
