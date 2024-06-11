import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfdeparture = pd.read_csv("departure.txt")
dfdeparture2 = pd.read_csv("departure 2.txt")
dfcountry_of_destination = pd.read_csv("country of destination.txt")

print(dfdeparture)

print(dfdeparture2)

print(dfcountry_of_destination)
####a)
dfdep = pd.concat([dfdeparture, dfdeparture2], axis = 0)
df_d = dfdep['department number'].value_counts()

df_d=df_d.to_frame().reset_index()
df_d.rename(columns=({'index':'department number','department number':'valeu of premise'}), inplace=True)

print(df_d)

#####б)
#df_d.plot(kind = 'bar')
#plt.show()
ax=df_d.plot(x='department number', y='valeu of premise',kind = 'bar')
plt.show()

######в)

dfdep=pd.merge(dfdep,dfcountry_of_destination ,on='destination country code')

dfdep['sum ']=dfdep['weight']*dfdep['price for delivery 1KH']
df3=dfdep[['department number','sum ']]

df3=df3.groupby('department number').sum()

print(df3)
####г)

df4=dfdep[['sum ','name']]
df4=df4.groupby('name').sum()
df4=df4.sort_values(by=['sum '],ascending=False)
t=df4.iloc[0]

print('\n','\n','\n',f"{t} have a maximum shipping cost")

####д)
print(df4)