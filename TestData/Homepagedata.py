class HomePageData:
    homepage_test_data = [
        {"name": "Pranay", "email": "pranay.ravula@gmail.com", "password": "Pranay@12"},
        {"name": "Uday", "email": "uday.ravula@gmail.com", "password": "Uday@12"},
    ]


# test cases taken from xl
# @staticmethod
# def data_from_xl(test_case):
#     # load the data
#     book = openpyxl.load_workbook("C:\\Users\\yjasw\\OneDrive\\Desktop\\Python\\workshet.xlsx")
#
#     # select the sheet from xl
#     sheet = book.active
#
#     Dict = {}
#     for i in range(1, sheet.max_row + 1):
#         if sheet.cell(row=i, column=1).value == test_case:
#             for j in range(2, sheet.max_column + 1):
#                 Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
#     return [Dict]
