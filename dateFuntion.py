import pandas as pd
from datetime import date
from  myfucntions import *
df=pd.read_csv('date22.csv')
df[['Date1','Date2']]=df[['Date1','Date2']].apply(pd.to_datetime)
df['new']=df['Date2'].dt.round('H')
print(df)