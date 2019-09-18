import pandas as pd

dict = {'#440140': {'document_id': '#440140', 'instrument_type': 'AGREEMENT', 'doc_date': ' 4/12/2019',
                    'rec_date': ' 5/22/2019', 'grantor': ['LALIM/GARRET L','LAXMI'],
                    'grantee': ['HESS BAKKEN INVESTMENTS II LLC','BORKAR'],
                    'legal': [' 157 93 18 W2NE4, N2SE4 ', ' 157 93 17 NW4SW4, SE4SW4 ']
                    }
        }
df = pd.DataFrame(dict)
df = df.reset_index()
df = df.set_index('index')
df = df.T
df = df.legal.apply(pd.Series).merge(df, left_index = True, right_index = True).drop(['legal'],axis=1).melt(id_vars=['doc_date','document_id','grantee','grantor','instrument_type','rec_date'], value_name='legal').drop(['variable'],axis=1)
df = df.grantor.apply(pd.Series).merge(df, left_index = True, right_index = True).drop(['grantor'],axis=1).melt(id_vars=['doc_date','document_id','grantee','legal','instrument_type','rec_date'], value_name='grantor').drop(['variable'],axis=1)
df = df.grantee.apply(pd.Series).merge(df, left_index = True, right_index = True).drop(['grantee'],axis=1).melt(id_vars=['doc_date','document_id','grantor','legal','instrument_type','rec_date'], value_name='grantee').drop(['variable'],axis=1)
print(df)