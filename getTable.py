def getTable(t,h,maxr,cmp,ws):
    m=0
    tab=[]
    a=h[m]
    b=t[m]
    wsh=[]
    while m<cmp:
        for r in range(1,maxr+1):
            for j in range(a,b):
                m=m+1
                tab.append(ws.cell(row=r,column=c).value)
    return tab