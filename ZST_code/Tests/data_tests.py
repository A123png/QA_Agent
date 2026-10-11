import pandas as pd

# 假设df是你的DataFrame
df = pd.read_csv('../data/query_from_others/query_data.csv')  # 或使用之前生成的DataFrame

# 转换为嵌套列表
data_list = df.values.tolist()
print(data_list[:3])  # 打印前3行查看