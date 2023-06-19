def copyall(maxr,maxc,ws,ws1):
    head_index=[]
    tab_index=[]
    for r in range (1, maxr + 1):
        for c in range (1, maxc + 1):
            if (ws.cell(row=r,column=c).value=='Data'):
                cmp=cmp+1            
                print(c,r)
                b=r
                for j in range(1,maxc+1):
                    for i in range(b+1,maxr+1):
                        ws1.cell(row=i,column=j).value=ws.cell(row=i,column=j).value
                    head_index.append([r,c]) 
                    tab_index.append([maxr,c-2])
    return head_index,tab_index,cmp