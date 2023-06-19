def infosheet(maxr,maxc,ws):
    startrowcol=[]
    endrowcol=[]
    startcols=[]
    endcols=[]
    totab=0
    unit=1
    for r in range (1, maxr + 1):
        for c in range (1, maxc + 1):
            if (ws.cell(row=r,column=c).value=='Data') and (ws.cell(row=r+1,column=c).value=='Unit'): 
                totab=totab+1            
                unit=r+1
                startrowcol.append([r,c]) 
                endrowcol.append([maxr,c-2])
                
    if totab!=0:
        endrowcol.remove([maxr,-1])
        endrowcol.append([maxr,maxc])
       
    for i in range(0,totab):                                                                      
        startcols.append(startrowcol[i][1])
        endcols.append(endrowcol[i][1])
        
    return totab,startrowcol,endrowcol,unit,startcols,endcols


