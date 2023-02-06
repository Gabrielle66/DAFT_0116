# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:16:04 2023

@author: Gaf
"""

import pandas as pd
import numpy as np
df = pd.read_csv(r'\Users\farah\DAFT_0116\Data clean\fake_job_postings.csv')

df.drop(['department','salary_range','benefits'], axis = 1, inplace = True) 
rows = df[(df['required_education'].isnull()==True) & (df['required_experience'].isnull()==True) & (df['function'].isnull()==True)]
drop_rows = list(rows.index)
df_clean = df.drop(drop_rows, axis=0) #rows