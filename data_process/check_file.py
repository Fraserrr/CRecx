
# recbole 要求输入的原子文件使用UTF-8和GBK编码都能打开
# 本函数分别进行检查
def check_file_encoding(file_path, encoding):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read()
            print(f"文件 {file_path} 使用 {encoding} 编码打开成功")
    except Exception as e:
        print(f"文件 {file_path} 使用 {encoding} 编码打开失败: {e}")


# 检查转换后的文件
files = ['hmx-400k.inter', 'hmx-400k.user', 'hmx-400k.item']
for file in files:
    check_file_encoding(file, 'gbk')
    check_file_encoding(file, 'utf-8')
