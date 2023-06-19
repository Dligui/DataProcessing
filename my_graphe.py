from recuperate_data_all_sheets import recuperate
from recuperate_data_all_sheets_head import copy_head
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt
import xlsxwriter

def my_graphe(path,DataRoom): # default value
    tab=copy_head(path,DataRoom)
    donnees=pd.DataFrame(tab)
    donnees.dropna(axis=0,inplace=True) # delete NaN
    donnees=donnees.drop([0],axis=0) # supprimer l head
    donnees = donnees.reset_index(drop=True)
    x=[]
    y=[]
    for i in range(1,532):
        if donnees[1][i]==donnees[1][i-1]:
            x.append(donnees[2][i])
            y.append(donnees[3][i])

        else:
            print(x,y)
            plt.plot(x,y)   #,grid=True,legend=True)
            plt.title('title name ')
            plt.xlabel('x_axis name')
            plt.ylabel('y_axis name')
            plt.show()
            x=[]
            y=[]
            print("new temperature")

    #res=all(ele==donnees[x] for ele in donnees[x])
    #if (res):


    # ax=donnees.plot(x=x,y=y,grid=True,legend=True)
    # ay=donnees.plot(x=x,y=4,grid=True,legend=True,ax=ax)
    # donnees.plot(x=x,y=5,grid=True,legend=True,ax=ay)
    # plt.title('title name')
    # plt.xlabel('x_axis name')
    # plt.ylabel('y_axis name')
    # plt.show()
    return donnees

path='C:/Users/zbptmj/Desktop/newdesk/py_gui/new_template.xlsx'
Data=my_graphe(path,'DataRoom') # if true ordre croissant -40...+25...

# add graphe : x & y : trier mes cols en fct de VIN OU TEMP ...
# supprimer des colonne   done
# differents tests    done
# sort cols           not completed

# charger excel file  --> choose head sheet --> recuperer tables --> convertir en dataframe -->faire le ordre en fct de temp C°,  les graphe , supression cols ...
# # --> conertir my dataframe en liste --> faire le paste dans calculus 

