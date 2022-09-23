import pandas as pd

d1 = pd.read_csv('data1.txt')
d2 = pd.read_csv('data2.txt')
df = pd.concat([d1, d2])
df = df.reset_index(drop=True)
print(df)
