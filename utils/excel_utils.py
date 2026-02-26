import openpyxl

def get_data_from_excel(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    total_rows = sheet.max_row
    total_cols = sheet.max_column
    print(total_rows)
    print(total_cols)

    for i in range(2, total_rows+1):
        for j in range(1, total_cols+1):
            print(sheet.cell(row=i, column=j).value)