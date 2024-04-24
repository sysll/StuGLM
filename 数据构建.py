import json
import pandas as pd
df = pd.read_excel("")
score = df[""]
Answer1 = df[""]
Answer2 = df[""]


# 假设用户输入多组内容，这里我们使用循环来模拟这个过程
for _ in range(Answer1.shape[0]):  # 假设用户要输入两组内容
    content = "该学生的语文成绩是，数学成绩是，英语成绩是，物理成绩是，化学成绩是，生物成绩是，。并且该生。的社交情况是"
    summary = input("请输入内容总结: ")

    # 构造单个产品的JSON对象
    product = {
        "content": content,
        "summary": summary
    }

    # 将单个产品的JSON对象转换为字符串并写入文件
    with open('products_info.json', 'a', encoding='utf-8') as jsonl_file:
        jsonl_file.write(json.dumps(product, ensure_ascii=False) + '\n')

print("数据已按JSON Lines格式保存到products_info.jsonl文件中。")