from recuperate_data_all_sheets import recuperate
from recuperate_data_all_sheets_head import copy_head
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt

def del_col(path,B,L,C,DataRoom): # default value
    tab=copy_head(path,DataRoom)
    donnees=pd.DataFrame(tab)
    donnees.dropna(axis=0,inplace=True) # delete NaN
    head=donnees.head(n=1) #  fisrt lines
    h=head.values.tolist()
    #donnees=donnees.drop(C,axis=0) # supprimer l head
    donnees.drop(columns=C,inplace=True)#supprimer une col
    donnees = donnees.reset_index(drop=True)
    print(donnees)
    tab=donnees.values.tolist()
    h.extend(tab)
    head=head.values.tolist()
    return head,h

path='C:/Users/zbptmj/Desktop/newdesk/py_gui/new_template.xlsx'
B=True ; L=[1] ; C=[10,11,12,13]# the user enter this values
Data=del_col(path,B,L,C,'DataRoom') # if true ordre croissant -40...+25...
#zero=Data[0].values.tolist()
print(Data[0],Data[1]) # 0: newhead , 1: h 

# add graphe
# supprimer une colonne
# differents tests