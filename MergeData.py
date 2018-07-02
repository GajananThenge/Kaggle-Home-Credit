# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 09:23:14 2018

@author: hp-pc
"""

import pandas as pd
import numpy as np

appli_test_df = pd.read_csv('application_train.csv')
bureau_df = pd.read_csv(r"I:\Kaggle Competition\all\bureau.csv")


result_df = pd.merge(appli_test_df,bureau_df_subset,on="SK_ID_CURR")

def merge_fk_SK_ID_CURR(df1,df2):
    try:
        return pd.merge(df1,df2,on="SK_ID_CURR")
    except Exception as e:
        return None



def merge_fk_SK_ID_BUREAU(df1,df2):
    try:
        return pd.merge(df1,df2,on="SK_ID_BUREAU")
    except Exception as e:
        return None
df1 = pd.read_csv('bureau.csv')
df2 = pd.read_csv('bureau_balance.csv')
result_df1 = merge_fk_SK_ID_BUREAU(df1,df2)
