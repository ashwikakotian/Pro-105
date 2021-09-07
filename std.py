import csv
import plotly.express as px
import pandas as pd
import math

with open ("std.csv" , newline="")as f:
    reader=csv.reader(f)
    fileData=list(reader)
data=fileData[0]
def mean (data):
    n=len (data)    
    total=0
    for x in data:
        total+=int(x)
    mean=total
    return mean
squredList=[]
for num in  data:
    a =int(num)-mean(data)
    a=a**2
    squredList.append(a)


sum=0
for i in squredList:
    sum+=i

result=sum/(len(data)-1)
std=math.sqrt(result)
print(std)
