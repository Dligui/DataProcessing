import win32com.client
# ExcelApp=win32com.client.GetActiveObject("Excel.Application")
# Wb=ExcelApp.Workbooks(2)
# ws=Wb.Worksheets(1)
# R=ws.Range("B1:B10")
# R.value=111111111

import xlwings as xw
#path='C:/Users/zbptmj/Desktop/newdesk/py_gui/new_template.xlsx'
wb = xw.books.active
sheet=wb.sheets.active
sheet['A1'].value = 2023
sheet['A2'].value = 'ghizlane'

# replace openpyxl by xlwings


# https://docs.xlwings.org/en/stable/reports.html#maxrows

