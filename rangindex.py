def rangindex(maxr,maxc,ws):
    startrowcol=[]
    endrowcol=[]
    totab=0
    endcol=1
    for r in range (1, maxr + 1):
        for c in range (1, maxc + 1):
            if (ws.cell(row=r,column=c).value=='Data'):
                totab=totab+1            
                #print(c,r)
                unit=r+1
                startrowcol.append([r,c]) 
                endcol=int(maxc/totab)
                #endrowcol.append([maxr,(maxc-1)/cmp])
    return startrowcol,endcol-1,unit,totab

