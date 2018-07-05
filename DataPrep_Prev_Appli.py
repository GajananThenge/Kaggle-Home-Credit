
import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.preprocessing import StandardScaler
from Utility import one_hot_encoder

def one_hot_encoder(data):
    cat_cols = list(data.select_dtypes(include=['object']).columns)
    for col in cat_cols:
        print(col)
        temp=pd.get_dummies(data[col],drop_first=True,prefix=col)
        temp.index=data.index
        data=pd.concat([data,temp],axis=1)
        print(data.shape)
    data=data.drop(cat_cols,axis=1)
    return data

def standard_scaling(data):
    id_list  = ['SK_ID_PREV','SK_ID_CURR']
    num_cols =  list(data.select_dtypes(exclude=['object']).columns)
    num_cols = list(set(num_cols) - set(id_list))
    
    features = data[num_cols]
    scaler = StandardScaler().fit(features.values)
    features = scaler.transform(features.values)
    data[num_cols] = features
    
    return data


def data_prep_prev_appli(file_path):
    try:
#        
#        selected_features = ['SK_ID_PREV','SK_ID_CURR','NAME_CONTRACT_TYPE',
#                             'AMT_ANNUITY','AMT_APPLICATION','AMT_CREDIT',
#                             'FLAG_LAST_APPL_PER_CONTRACT',
#                             'NFLAG_LAST_APPL_IN_DAY','NAME_CASH_LOAN_PURPOSE',
#                             'NAME_CONTRACT_STATUS','CODE_REJECT_REASON','NAME_CLIENT_TYPE',
#                             'NAME_GOODS_CATEGORY','NAME_PORTFOLIO']
        prev_app_df = pd.read_csv(file_path,usecols=['SK_ID_PREV','SK_ID_CURR','NAME_CONTRACT_TYPE',
                             'AMT_ANNUITY','AMT_APPLICATION','AMT_CREDIT',
                             'FLAG_LAST_APPL_PER_CONTRACT',
                             'NFLAG_LAST_APPL_IN_DAY','NAME_CASH_LOAN_PURPOSE',
                             'NAME_CONTRACT_STATUS','CODE_REJECT_REASON','NAME_CLIENT_TYPE',
                             'NAME_GOODS_CATEGORY','NAME_PORTFOLIO'])
        
#        prev_app_df.isnull().sum()
        prev_app_df['AMT_ANNUITY'] = prev_app_df['AMT_ANNUITY'].fillna(0)
    
        prev_app_df = prev_app_df.dropna()
        
        #Standard Scaling on numeric data
        scaled_data = standard_scaling(prev_app_df)
        
        #One hot encodiing on categorial data
        data = one_hot_encoder(scaled_data)
        
        return data
    except Exception as e:
        print(e)
        return e
        
#        g = df.columns.to_series().groupby(df.dtypes).groups
#        col_list = list(df.columns.values)
#        
#        cat_data_col = list(df.select_dtypes(include=['object']).columns)
        
#        
#        
#file_path = r'D:\Personal\Kaggle\HomeCredit\all\previous_application.csv'
#result = data_preprocessing_prev_appli(file_path)
