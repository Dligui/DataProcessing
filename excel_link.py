import pandas as pd 
import openpyxl  

mesfichiers=['C:/Users/ZBPTMJ/Downloads/january.xlsx','C:/Users/ZBPTMJ/Downloads/february.xlsx','C:/Users/ZBPTMJ/Downloads/march.xlsx'] # La listes des chemins des fichiers excel

#dataframe pour passer apres au format excel
fichier_combine=pd.DataFrame() #objet data frame pour combiner les fichiers 

#combiner tous les fichiers
# for monfichier in mesfichiers :
#     df=pd.read_excel(monfichier,skiprows=3)
#     print(df)
#     fichier_combine=fichier_combine.append(df,ignore_index=True)


#fichier_combine.to_excel('fichier_combine.xlsx')

# collecter le contenu d'une cellule à partir de plusieurs cellules
valeurs=[] # liste
valeurs_dict={} #dictionnaire pour passer de liste à dataframe pour le mettre sous format excel

# for monfichier in mesfichiers:
#     wb=openpyxl.load_workbook(monfichier)
#     sheet=wb['Sheet1']
#     valeur=sheet['F5'].value  # chercher la valeur de la cellule F5 
#     valeurs.append(valeur)

# valeurs_dict['valeurs']=valeurs

# pd.DataFrame(valeurs_dict).to_excel('valeurs_toronto.xlsx')
#afficher la liste des valeurs collectées
print('la liste :',valeurs)
print('le dictionnaire :',valeurs_dict)


#operation sur des cellules excel : total de la collone F5 à F8  : le resultat sera dans F9 

for monfichier in mesfichiers:
    wb=openpyxl.load_workbook(monfichier)
    sheet=wb['Sheet1']
    sheet['F9']='=SUM(F5:F8)'
    sheet['F9'].style='Currency'
    sheet['E9']='total global'
    wb.save(monfichier)