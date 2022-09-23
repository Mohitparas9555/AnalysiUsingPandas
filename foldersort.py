import pandas as pd
import os
df = pd.read_csv('simple.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day_name()

y = list(df['Year'].unique())
path = r'C:\Users\Admi\OneDrive\Desktop\yeardata'
for i in y:
    yp = path+ '\\' + str(i)
    os.mkdir(yp)
    ef = df.loc[df['Year']==i]
    m = list(ef['Month'].unique())
    for j in m:
        mp= yp + '\\' + str(j)
        os.mkdir(mp)
        ff = ef.loc[df['Month'] == j]
        d = list(ff['Day'].unique())
        for k in d:
            dp = mp + '\\' + str(k)
            os.mkdir(dp)
            gf = ff.loc[ff['Day']==k]
            gf.to_csv(dp+'\\'+ str(i) + str(j) + str(k) + '.csv',index=False)
