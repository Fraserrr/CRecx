import unicodedata

# 从数据表格转换 recbole 需要的 item 类型原子文件

# 定义要保存的文本内容
text_content = """c_id:token\tcourse_code:token\tfull_title:token_seq
5\tCB22x\tThe Ancient Greek Hero
1\tCS50x\tIntroduction to Computer Science I
3\tER22x\tJustice
2\tPH207x\tHealth in Numbers: Quantitative Methods in Clinical & Public Health Research
4\tPH278x\tHuman Health and Global Environmental Change
6\t14.73x\tThe Challenges of Global Poverty
13\t2.01x\tElements of Structures
12\t3.091x\tIntroduction to Solid State Chemistry
8\t6.002x\tCircuits and Electronics
7\t6.00x\tIntroduction to Computer Science and Programming
10\t7.00x\tIntroduction to Biology
9\t8.02x\tElectricity and Magnetism
11\t8.MReV\tMechanics Review"""

def clean_text_for_gbk(text):
    """
    清洗文本以确保其可以在GBK编码中表示。
    替换掉所有不在GBK编码范围内的字符。
    """
    cleaned_text = []
    for char in text:
        try:
            # 尝试将字符编码为GBK
            char.encode('gbk')
            cleaned_text.append(char)
        except UnicodeEncodeError:
            # 如果编码失败，则替换为'?'字符
            cleaned_text.append('?')
    return ''.join(cleaned_text)

# 保存为UTF-8编码的文件
utf8_output_path = 'hmx-400k.item'
with open(utf8_output_path, 'w', encoding='utf-8') as file:
    file.write(text_content)

print(f"原子文件已保存为 {utf8_output_path}")
