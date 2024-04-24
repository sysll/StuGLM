import pandas as pd

import pandas as pd

# 读取Excel文件
file_path = '2022数统名单1.xlsx'  # 替换为您的Excel文件路径
sheet_name = 'Sheet1'  # 替换为您的工作表名称
df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')

# 筛选地址列中前三个字符是“福建省”的行，并只保留指定列
filtered_df = df[df['地址'].str.startswith('福建省')][['姓名','地址', '语文', '数学', '英语']]

# 显示筛选后的数据
print(filtered_df)

# 如果需要，您可以将筛选后的数据保存到新的Excel文件
output_file_path = '清洗后的数据.xlsx'  # 输出文件的路径
filtered_df.to_excel(output_file_path, index=False, engine='openpyxl')