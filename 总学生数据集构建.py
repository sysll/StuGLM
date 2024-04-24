import pandas as pd

# 读取两个 Excel 文件为 DataFrame
df1 = pd.read_excel('studata.xlsx')
df2 = pd.read_excel('清洗后的数据.xlsx')

# 合并两个 DataFrame，根据姓名进行匹配
merged_df = pd.merge(df1, df2, on='姓名', how='left')

# 打印合并后的 DataFrame，可以根据实际情况调整输出的列
print(merged_df)

merged_df.to_excel('merged_data.xlsx', index=False)