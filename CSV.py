import csv


# Display all the Column Names
#
# with open("School_Nutrition.csv") as csv_file:
#     csv_reader=csv.reader(csv_file)
#     print("Column names are")
#     i=next(csv_reader)
#     print(i)

column_names=['ProgramYear', 'ReportType', 'CEID', 'CEName', 'CECounty', 'ESC']

# Display first 10 column names in a List
with open("School_Nutrition.csv",encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for i, row in reader:
        print(row[i])
        row_count = sum(1 for row in reader)
    print(row_count)


#     header=next(reader)
#     print(reader)
#     print(header)
#     list1=[]
#     for i in range(1,10):
#         for row in header:
#             list1.append(row)
# print(list1)

# # Display first 10 column names in a List
# with open("School_Nutrition.csv",encoding='utf-8-sig') as file:
#     data=csv.reader(file,delimiter=',')
#     header=next(data)
#     list1=[]
#     for i in range(1,10):
#         for row in header:
#             list1.append(row)
# print(list1)

import pandas

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

