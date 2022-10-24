import xlsxwriter

workbook = xlsxwriter.Workbook('/home/user/Desktop/test.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

workbook.close()