import pandas as pd
df = pd.read_excel("测试集的excel.xlsx")
subject = ['语文',' 数学','英语', '物理', '化学', '生物', '政治', '地理']

score = []
a_score_string = ["某学生的"]
all_stu_score_string = []

for i in range(df.shape[0]):#读取contnet部分
    score1 = df['语文'][i]
    score.append(score1)
    score2 = df['数学'][i]
    score.append(score2)
    score3 =df['英语'][i]
    score.append(score3)
    score4 = df['物理成绩'][i]
    score.append(score4)
    score5 =df['化学成绩'][i]
    score.append(score5)
    score6 =df['生物成绩'][i]
    score.append(score6)
    score7 =df['政治成绩'][i]
    score.append(score7)
    score8 =df['地理成绩'][i]
    score.append(score8)

    experience1 = df['社交经历'][i]
    experience2 = df['学科综合经历'][i]

    for j in range(8):  #把该学生的成绩合成一段话作为总成绩
        if score[j] !=0 :
            a_score_string.append(f"{subject[j]}成绩是{score[j]}，")

    a_score_string.append(f'该学生的社交经历包括：{experience1}')
    a_score_string.append(f'，该学生的竞赛经历包括：{experience2}。')
    a_score_string.append('请你作为学生评估系统，评估该学生的社交能力。回答我该学生社交能力的星级，并且解释原因。')
    result = "".join(a_score_string) #一个学生的所有回答
    all_stu_score_string.append(result)
    a_score_string = ["某学生的"]
    score = []

# print(len(all_stu_score_string))  #各个学生的content


all_label = []
label = ['该学生的星级是：']
for i in range(df.shape[0]):
    remark1 = df['社交能力'][i]
    label.append(remark1)

    label.append("。原因是：")

    remark2 = df['理由'][i]
    label.append(remark2)

    result = "".join(label)
    all_label.append(result)

    label = ['该学生的星级是：']
# print(len(all_label)) #各个学生的

import json
#列表转json
for i in range(df.shape[0]):  # 假设用户要输入两组内容
    content = all_stu_score_string[i]
    summary = all_label[i]

    # 构造单个产品的JSON对象
    product = {
        "content": content,
        "summary": summary
    }

    # 将单个产品的JSON对象转换为字符串并写入文件
    with open('val.json', 'a', encoding='utf-8') as jsonl_file:
        jsonl_file.write(json.dumps(product, ensure_ascii=False) + '\n')

print("数据已按JSON Lines格式保存到products_info.jsonl文件中。")