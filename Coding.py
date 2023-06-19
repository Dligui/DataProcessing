import xlwings as xw 
import pandas as pd 
import matplotlib.pyplot as plt
# https://www.youtube.com/watch?v=4CrZUJtjZkc
# 

wb=xw.Book()
sht=wb.sheets[0]
sht.name="Report"
sht['A1']='onsemi Internal Use Only'

fig=plt.figure()
x=df["day"]
y=df["total_bill"]
plt.bar(x,y)
plt.ylabel("in USD")
plt.title("Total Bill by Day")

sht.add(fig,name="Graph",update=True,left=sht.range("A4").left,top=sht.range("A4").top,height=200,width=300,)

print("done")
wb.save()
