import xlsxwriter
import random

def graph(path,x,y):
    random_data = [random.random() for _ in range(10)]
    # Data location inside excel
    data_start_loc = [0, 0] # xlsxwriter rquires list, no tuple
    data_end_loc = [data_start_loc[0] + len(random_data), 0]

    path='C:/Users/zbptmj/Desktop/newdesk/py_gui/Nouveau.xlsx'
    workbook = xlsxwriter.Workbook(path)

    # Charts are independent of worksheets
    chart = workbook.add_chart({'type': 'line'})
    chart.set_y_axis({'name': 'Random jiggly bit values'})
    chart.set_x_axis({'name': 'Sequential order'})
    chart.set_title({'name': 'Insecure randomly jiggly bits'})
    worksheet = workbook.add_worksheet()

    # A chart requires data to reference data inside excel
    worksheet.write_column(*data_start_loc, data=random_data)
    # The chart needs to explicitly reference data
    chart.add_series({
        'values': [worksheet.name] + data_start_loc + data_end_loc,
        'name': "Random data",
    })

    worksheet.insert_chart('F1', chart)

    workbook.close()  # Write to file