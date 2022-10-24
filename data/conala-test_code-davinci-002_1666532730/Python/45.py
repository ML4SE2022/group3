import xlrd

# Open the workbook and define the worksheet
book = xlrd.open_workbook("file.xls")
sheet = book.sheet_by_name("Sheet1")

# Extract and print all of the values
data = [sheet.row_values(i) for i in range(sheet.nrows)]

# Write data to a file
with open('file.txt', 'w') as f:
    for line in data:
        f.write(str(line) + '\n')