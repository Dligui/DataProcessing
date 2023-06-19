from recuperate_data_all_sheets import recuperate
from recuperate_data_all_sheets_head import copy_head
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt

def sorted_tab(path,B,L,DataRoom): # default value
    tab=copy_head(path,DataRoom)
    #tab=recuperate(path)
    donnees=pd.DataFrame(tab)
    donnees.dropna(axis=0,inplace=True) # delete NaN
    head=donnees.head(n=1) #  fisrt lines
    h=head.values.tolist()
    donnees=donnees.drop([0],axis=0) # supprimer l head
    #donnees = donnees.reset_index(drop=True) #drop=True)
    print(donnees.sort_values(by=L,ascending=B, inplace=True))#.reset_index(drop = True))  # sorte temp and pvin columns
    donnees = donnees.reset_index(drop=True)#,axis=0) #drop=True)
    #donnees.drop(['temp','VPIN1','Reg13'],axis=1,inplace=True)#supprimer une col
    tab=donnees.values.tolist()
    h.extend(tab)
    head=head.values.tolist()
    return head,h

# path='C:/Users/zbptmj/Desktop/newdesk/py_gui/new_template.xlsx'
# B=True ; L=[1] # the user enter this values
# Data=sorted_tab(path,B,L,'DataRoom') # if true ordre croissant -40...+25...
# #zero=Data[0].values.tolist() 
# print(Data[1]) # 0: newhead , 1: h 

# add graphe
# supprimer une colonne
# differents tests