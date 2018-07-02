# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 19:09:33 2018

@author: hp-pc
"""



def data_preprocessing_application(file_path):
    try:
        import pandas as pd
        import numpy as np
        from sklearn.preprocessing import Imputer
        #from sklearn.preprocessing import LabelEncoder,OneHotEncoder
        from sklearn.preprocessing import StandardScaler
        #Read df
        df = pd.read_csv(file_path)
        
#        #Handling missing columns names AMT_ANNUITY
#        imputer=Imputer(missing_values = np.NAN, strategy='mean', axis=0)
#        df['AMT_ANNUITY'] = imputer.fit_transform(df['AMT_ANNUITY'].values.reshape(-1,1))
#        
#        #Handling missing columns names AMT_GOODS_PRICE
#        #AMT_GOODS_PRICE = For consumer loans it is the price of the goods for which the loan is given
#        imputer_goods_price=Imputer(missing_values = np.NAN, strategy='mean', axis=0)
#        df['AMT_GOODS_PRICE'] = imputer_goods_price.fit_transform(df['AMT_GOODS_PRICE'].values.reshape(-1,1))
        

        df['AMT_ANNUITY'].replace(np.NaN,0.0,inplace=True)

        df['AMT_GOODS_PRICE'].replace(np.NaN,0.0,inplace=True)
        
        df['OWN_CAR_AGE'].replace(np.NaN,0.0,inplace=True)
        
        #Family count default one
        df['CNT_FAM_MEMBERS'].replace(np.NaN,1.0,inplace=True)
        
        
        #Scaling
        # OWN_CAR_AGE
        sc_own_car_age = StandardScaler()
        sc_own_car_age=sc_own_car_age.fit_transform(df['OWN_CAR_AGE'].values.reshape(-1,1))
        df['OWN_CAR_AGE'] = sc_own_car_age
        
        sc_amt_income_total= StandardScaler()
        sc_amt_income_total=sc_amt_income_total.fit_transform(df['AMT_INCOME_TOTAL'].values.reshape(-1,1))
        df['AMT_INCOME_TOTAL'] = sc_amt_income_total
        
        sc_amt_credit = StandardScaler()
        sc_amt_credit = sc_amt_credit.fit_transform(df['AMT_CREDIT'].values.reshape(-1,1))
        df['AMT_CREDIT'] = sc_amt_credit
        
        sc_amt_annuity= StandardScaler()
        sc_amt_annuity=sc_amt_annuity.fit_transform(df['AMT_ANNUITY'].values.reshape(-1,1))
        df['AMT_ANNUITY'] = sc_amt_annuity
        
        sc_amt_goods_price = StandardScaler()
        sc_amt_goods_price=sc_amt_goods_price.fit_transform(df['AMT_GOODS_PRICE'].values.reshape(-1,1))
        df['AMT_GOODS_PRICE'] = sc_amt_goods_price
        
        #Group2 
        df[['YEARS_BEGINEXPLUATATION_AVG','YEARS_BUILD_AVG',
                 'COMMONAREA_AVG','ELEVATORS_AVG','ENTRANCES_AVG',
                 'FLOORSMAX_AVG','FLOORSMIN_AVG','LANDAREA_AVG',
                 'LIVINGAPARTMENTS_AVG','LIVINGAREA_AVG',
                 'NONLIVINGAPARTMENTS_AVG','NONLIVINGAREA_AVG','APARTMENTS_MODE',
                 'BASEMENTAREA_MODE','YEARS_BEGINEXPLUATATION_MODE','EXT_SOURCE_1',
                 'EXT_SOURCE_2','EXT_SOURCE_3','APARTMENTS_AVG','BASEMENTAREA_AVG']]= df[['YEARS_BEGINEXPLUATATION_AVG','YEARS_BUILD_AVG',
                 'COMMONAREA_AVG','ELEVATORS_AVG','ENTRANCES_AVG',
                 'FLOORSMAX_AVG','FLOORSMIN_AVG','LANDAREA_AVG',
                 'LIVINGAPARTMENTS_AVG','LIVINGAREA_AVG',
                 'NONLIVINGAPARTMENTS_AVG','NONLIVINGAREA_AVG','APARTMENTS_MODE',
                 'BASEMENTAREA_MODE','YEARS_BEGINEXPLUATATION_MODE','EXT_SOURCE_1',
                 'EXT_SOURCE_2','EXT_SOURCE_3','APARTMENTS_AVG','BASEMENTAREA_AVG']].fillna(0)
        
        #Group3
        df[['YEARS_BUILD_MODE']].fillna(0, inplace=True)
        df['COMMONAREA_MODE'].fillna(0, inplace=True)
        df['ELEVATORS_MODE'].fillna(0, inplace=True)
        df['ENTRANCES_MODE'].fillna(0, inplace=True)
        df['FLOORSMAX_MODE'].fillna(0, inplace=True)
        df['FLOORSMIN_MODE'].fillna(0, inplace=True)
        df['LANDAREA_MODE'].fillna(0, inplace=True)
        df['LIVINGAPARTMENTS_MODE'].fillna(0, inplace=True)
        df['LIVINGAREA_MODE'].fillna(0, inplace=True)
        df['NONLIVINGAPARTMENTS_MODE'].fillna(0, inplace=True)
        df['NONLIVINGAREA_MODE'].fillna(0, inplace=True)
        df['APARTMENTS_MEDI'].fillna(0, inplace=True)
        df['BASEMENTAREA_MEDI'].fillna(0, inplace=True)
        df['YEARS_BEGINEXPLUATATION_MEDI'].fillna(0, inplace=True)
        df['YEARS_BUILD_MEDI'].fillna(0, inplace=True)
        df['COMMONAREA_MEDI'].fillna(0, inplace=True)
        df['ELEVATORS_MEDI'].fillna(0, inplace=True)
        df['ENTRANCES_MEDI'].fillna(0, inplace=True)
        df['FLOORSMAX_MEDI'].fillna(0, inplace=True)
        df['FLOORSMIN_MEDI'].fillna(0, inplace=True)
        df['LANDAREA_MEDI'].fillna(0, inplace=True)
        df['LIVINGAPARTMENTS_MEDI'].fillna(0, inplace=True)
        df['LIVINGAREA_MEDI'].fillna(0, inplace=True)
        df['NONLIVINGAPARTMENTS_MEDI'].fillna(0, inplace=True)
        df['NONLIVINGAREA_MEDI'].fillna(0, inplace=True)
        df['FONDKAPREMONT_MODE'].fillna(0, inplace=True)
        df['HOUSETYPE_MODE'].fillna(0, inplace=True)
        df['TOTALAREA_MODE'].fillna(0, inplace=True)
        df['WALLSMATERIAL_MODE'].fillna(0, inplace=True)
        df['EMERGENCYSTATE_MODE'].fillna(0, inplace=True)
        
        #Gp4
        df[['AMT_REQ_CREDIT_BUREAU_HOUR',
            'AMT_REQ_CREDIT_BUREAU_DAY','AMT_REQ_CREDIT_BUREAU_WEEK','AMT_REQ_CREDIT_BUREAU_MON',
            'AMT_REQ_CREDIT_BUREAU_QRT','AMT_REQ_CREDIT_BUREAU_YEAR','YEARS_BUILD_MODE',
            'OBS_30_CNT_SOCIAL_CIRCLE','DEF_30_CNT_SOCIAL_CIRCLE','OBS_60_CNT_SOCIAL_CIRCLE'
            ,'DEF_60_CNT_SOCIAL_CIRCLE','DAYS_LAST_PHONE_CHANGE']] = df[['AMT_REQ_CREDIT_BUREAU_HOUR',
                                                                 'AMT_REQ_CREDIT_BUREAU_DAY','AMT_REQ_CREDIT_BUREAU_WEEK','AMT_REQ_CREDIT_BUREAU_MON',
                                                                 'AMT_REQ_CREDIT_BUREAU_QRT','AMT_REQ_CREDIT_BUREAU_YEAR','YEARS_BUILD_MODE',
                                                                 'OBS_30_CNT_SOCIAL_CIRCLE','DEF_30_CNT_SOCIAL_CIRCLE','OBS_60_CNT_SOCIAL_CIRCLE',
                                                                 'DEF_60_CNT_SOCIAL_CIRCLE','DAYS_LAST_PHONE_CHANGE']].fillna(0)
        
        
        #Convert all Categorical data into one_hot encoder
        result_df= pd.get_dummies(df,dummy_na=True)
        
        #Uncomment Below line to save the result dataframe
        #result_df.to_csv(r'I:\Kaggle Competition\Home Credit\MasterData.csv',index=False)
        return result_df
    except Exception as e:
        print(e)

file_path = r'application_train.csv'

data_preprocessing_application(file_path)