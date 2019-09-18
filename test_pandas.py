import pandas as pd

# dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
#        "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
#        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
#        "population": [200.4, 143.5, 1252, 1357, 52.98] }

# df = pd.DataFrame(dict)
# print(df)
#----------------------------------------------------------------------------------------------------------------

# dtype={'ProgamYear':str,'Report_Type':str,'CEID':int,'CEName':str,'CECounty':str}
#
# df = pd.read_csv('/Users/akhilavemuganti/Desktop/PythonWorkSpace/HelloWorld/School_Nutrition.csv',
#             delimiter=',', names=['ProgramYear','Report_Type','CEID','CEName','CECounty'], low_memory=False)
#
# print(df.head(3)

#----------------------------------------------------------------------------------------------------------------
# zoo_detais = pd.read_csv('/Users/akhilavemuganti/Desktop/PythonWorkSpace/HelloWorld/Zoo.csv',delimiter=',')
# print(zoo_detais)
#----------------------------------------------------------------------------------------------------------------

# txt=pd.read_csv('/Users/akhilavemuganti/Desktop/PythonWorkSpace/HelloWorld/pandas_tutorial_read.csv',
#                 delimiter=',',names=['My_datetime','event','country','user_id','source','topic'])
# print(txt)
# print(txt.head()) #Print first 5 rows of data
# print(txt.tail()) #Print first 5 rows of data
# print(txt.sample(5)) #Random 5 records

# print(txt[['country','user_id','topic']][txt.country=='country_2'].head())

# Aggregation Functions

# print(txt.groupby('source').count()[['My_datetime','user_id']])
# print(txt[txt.country=='country_2'].groupby(['source','topic']).count())
#----------------------------------------------------------------------------------------------------------------

# zoo_details = pd.read_csv('/Users/akhilavemuganti/Desktop/PythonWorkSpace/HelloWorld/Zoo.csv',delimiter=',')
# # print(zoo_details)
# zoo_eats = pd.read_csv('/Users/akhilavemuganti/Desktop/PythonWorkSpace/HelloWorld/Zoo_eats.csv',delimiter=',')
#     # DataFrame([['elephant','vegetables'], ['Tiger','meat'], ['Kangaroo','vegetables'],
#     #            ['Zebra','vegetables'], ['Giraffe','vegetables']], columns=['Animal','food'])
#
# # print(zoo_eats)
# # print(zoo_details.merge(zoo_eats))
# print(zoo_details.count())
#
#
# dict= {'document_id': '#440140', 'instrument_type': 'AGREEMENT',
#  'doc_date': ' 4/12/2019', 'rec_date': ' 5/22/2019',
#  'grantor': ['LALIM/GARRET L'],
#  'grantee': ['HESS BAKKEN INVESTMENTS II LLC'],
#  'legal': ['    157 93 18     W2NE4, N2SE4 ', '    157 93 17     NW4SW4, SE4SW4 ']
#  }
#
# print(dict)
# df = pd.DataFrame(dict)
# print(df)



dict = {'#440140': {'document_id': '#440140', 'instrument_type': 'AGREEMENT', 'doc_date': ' 4/12/2019',
'rec_date': ' 5/22/2019', 'grantor': ['LALIM/GARRET L'], 'grantee': ['HESS BAKKEN INVESTMENTS II LLC'],
'legal': [' 157 93 18 W2NE4, N2SE4 ', ' 157 93 17 NW4SW4, SE4SW4 ']
}
}
df = pd.DataFrame(dict)
df = df.reset_index()
df = df.set_index('index').T
print(df)