from recuperate_data_all_sheets import recuperate
from recuperate_data_all_sheets_head import copy_head
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt

def del_col(path,C,DataRoom): # default value
    tab=copy_head(path,DataRoom)
    donnees=pd.DataFrame(tab)
    donnees.dropna(axis=0,inplace=True) # delete NaN
    donnees.drop(columns=C,inplace=True)#supprimer une col
    donnees = donnees.reset_index(drop=True)
    return donnees

path='C:/Users/zbptmj/Desktop/newdesk/py_gui/new_template.xlsx'
C=[10,11,12,13]# the user enter this values
Data=del_col(path,C,'DataRoom') # if true ordre croissant -40...+25...
print(Data) # 0: newhead , 1: h 

# add graphe
# supprimer des colonne   done
# differents tests    done
# sort cols           not completed