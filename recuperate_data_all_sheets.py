from Tab_Sheets import Tab_sheets
from copy_paste_ranges1 import copy_paste_ranges1
from pasteRange import pasteRange
from openpyxl import  load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from operator import itemgetter
import pandas as pd 
def recuperate(path):
    datasheets=Tab_sheets(path)
    data=[]
    info=[]
    tabs=[]
    # head=[]
    # ftab=[]
    for i in range(0,len(datasheets)):
        if type(datasheets[i])== str:
            data.append(datasheets[i]) # sheets_names
        else:
            info.append(datasheets[i]) #info sheets
    for i in range(0,len(data)):
        tabs.extend(copy_paste_ranges1(path,data[i])) # all data
    
    return tabs

#Function test
# path='C:/Users/zbptmj/Desktop/newdesk/py_gui/new_template.xlsx'
# wb=load_workbook(path)
# tabs=recuperate(path)
# print(len(tabs),tabs) # len -1

