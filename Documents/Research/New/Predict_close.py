import pandas
import numpy as np
import os as oss


arr = oss.listdir()
print(arr)

for k in range(len(arr)):

 temp = arr[k]

 df = pandas.read_csv(temp)
 close = []
 open = []
 z = 0

 for x in range(len(df)):

     close.append(np.array(df.iloc[x][2]))
     open.append(np.array(df.iloc[x][1]))


 for y in range(len(close)-2):
     if ((close[y]-open[y] >= 0 and close[y+1]-open[y+1] >= 0) or (close[y]-open[y] <= 0 and close[y+1]-open[y+1] <= 0)):
          z = z+1


 print("value for", temp,(z/(len(close)-2))*100, z, len(df), len(close))

