import pandas as pd
import numpy as np
df=pd.read_csv('date22.csv')
df['Date1']=pd.to_datetime(df['Date1'])
df['Date2']=pd.to_datetime(df['Date2'])
#df=df.loc[df['Date2']>='2011']
df=df.set_index('Date2')
df=df.sort_index()
df=df.loc['2010-02':'2011-03']
df=df.reset_index()
print(df[['Date2','Date1']])

print(df.info())
