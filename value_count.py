import pandas as pd
df=pd.read_csv('walmart.csv')

print(df['Type'].value_counts(normalize=True))
print(df.groupby('Type')['Type'].count())