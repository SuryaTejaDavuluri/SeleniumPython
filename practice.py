import xlrd


workbook = xlrd.open_workbook("C:/Users/RC08508/PycharmProjects/SeleniumPython/TestData/testdata.xlsx")
sheet = workbook.sheet_by_name("SelectDropdown")

rowCount = sheet.nrows
colCount = sheet.ncols
print(rowCount)
print(colCount)

for curr_row in range(1, rowCount):
    statesExcel = sheet.cell_value(curr_row, 0)
    items = [statesExcel]
    print(items)

    for i in range(len(items)):
        print(items[i])
        y = items[i]
        z = y.split(':')
        print(z)
        for k in range(len(z)):
            print(z[k])

