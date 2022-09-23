import pandas as pd
d1=pd.read_csv('data1.txt')
d2=pd.read_csv('data2.txt')
df=d1.merge(d2,on='id')
print(df)