import pandas as pd

# 为原始文件增加整数递增的用户ID和课程ID

# 读取原始CSV文件
input_file = 'hmx_selected.csv'
output_file = 'hmx_int_id.csv'

df = pd.read_csv(input_file)

# 为user_id创建映射关系并添加u_id列
unique_users = df['user_id'].unique()
user_id_to_int = {user_id: idx for idx, user_id in enumerate(unique_users, start=1)}
df['u_id'] = df['user_id'].map(user_id_to_int)

# 为course_code创建映射关系并添加c_id列
unique_courses = df['course_code'].unique()
course_code_to_int = {course_code: idx for idx, course_code in enumerate(unique_courses, start=1)}
df['c_id'] = df['course_code'].map(course_code_to_int)

# 保存结果到新的CSV文件
df.to_csv(output_file, index=False)

print(f"已成功转换并将结果保存到 {output_file}")