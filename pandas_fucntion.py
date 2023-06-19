import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt
filename=""
donnees=pd.read_excel(filename,sep=';')
print(donnees)
print(donnees.shape) # taille du fichier row col
print(donnees.columns) # l'entete du fichier
print(donnees.head()) # 5 fisrt lines
print(type.donnees) # dataframe objet pandas
print(donnees['Temp']) # recuperer la colonne du temperatures
print(type(donnees['temp']))# series 
print(donnees.loc[5])# recuperer la ligne 5 du donnees avec l'entete
print(donnees.loc[[5]]) # exactement la ligne 5 horizental
print(donnees.iloc[5,6]) # val du ligne 5 col 6
print(donnees.iloc[5:8,6:9]) # recuperer un  tableau dans un tableau
print(donnees['temp'][5:10]) # les 5 ligne de temp
print(donnees.drop([0,1,2],axis=0),inplace=True) # supprimer data axis=0 ligne axis =1 colone faut inplace to   save
donnees.dropna(axis=0,inplace=True) # delete NaN
print(donnees) # delete NaN
donnees.drop(['temp','VPIN1','Reg13'],axis=1,inplace=True)#supprimer une col
print(donnees) 
print(donnees.describe()) # 
# convertir data str en un type pour faire le calcul
donnees['temp']=donnees['temp'].astype(float) # non
donnees['temp']=='-' # true or false
print(donnees[donnees['temp']=='-']) # les info des ligne contient des tirés --
ind=donnees[donnees['temp']=='-'].index
print(ind) # les index des lgnes avec des tirés pour les supprimer
donnees.drop(ind,axis=0,inplace=True) # supprimer ses lignes 
donnees['temp']=donnees['temp'].astype(float) # format numeric definir les types de mon data
print(donnees.describe()) # mean min std max count 25%
print(donnees['temp']>10.0) # true or false 
print(donnees[donnees['temp']>10.0]) # tout les lgne avec cet condition
donnees['time']=pd.to_datetime(donnees['time'],format="%d%d/%d%d/%d%d%d%d") 
print(donnees['market'].value_counts())# 
donnees['market'].value_counts().plot.pie() # graphe des data
plt.show()
donnees['market'].value_counts().plot.bar() # graphe des data
plt.show()
print(donnees.groupby(['market']).mean()) # la val moyenne







from recuperate_data_all_sheets import recuperate
from recuperate_data_all_sheets_head import copy_head
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt

def sorted_tab(path):
    tab=copy_head(path,'DataRoom')
    donnees=pd.DataFrame(tab)
    #print(donnees[1])
    #print(donnees.shape) # taille du fichier row col
    #print(donnees.columns) # l'entete du fichier
    donnees.dropna(axis=0,inplace=True) # delete NaN
    #print(donnees.loc[[0][0]][0]) # Unit
    # ind=donnees[donnees[5]=='-'].index
    # print(ind) # les index des lgnes avec des tirés pour les supprimer
    # donnees.drop(ind,axis=0,inplace=True) # supprimer ses lignes 
    #print(donnees.describe()) # 
    # donnees[3].value_counts().plot.bar() # graphe des data
    # plt.show()
    #donnees=sorted(donnees, key=lambda x: x[4])
    #print(donnees[4])
    donnees=donnees.drop([0],axis=0) # supprimer lhead
    print(donnees.sort_values(by=[1,2],ascending=True, inplace=True))#.reset_index(drop = True))
    donnees = donnees.reset_index(drop=True)
    print(donnees)
    tab=donnees.values.tolist()
    return tab

    

#    Unit  Temp (°C)  V_PVIN3*PVIN2*VINLDO (V)  ...  REG_04 - INTERRUPT_FLAG_IC[All] MCU()  REG_05 - INTERRUPT_FLAG_ERR1[All] MCU()  IoutMax(mA)
path='C:/Users/zbptmj/Desktop/newdesk/py_gui/new_template.xlsx'
sorted_tab(path)
    
