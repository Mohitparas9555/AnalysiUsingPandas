import pandas as pd
df = pd.read_csv('pokemon.csv')
l=[]
for i,v in df.iterrows():
    l.append(v['Speed'])
print(l)