#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import ipynbname

file1 = "D:\\DATA\\1050201New\\113校外實習書面審查作業\\0000_校庫資料_11210學10.學生實習人數及時數(10月填報).xlsx"

df1 = pd.read_excel(file1)

print(len(df1))
print(df1.columns)

df1.head()


# In[2]:


# 透過ipynbname模組取得檔名
nb_fname = ipynbname.name()
print(nb_fname)

try:   
    get_ipython().system('jupyter nbconvert --output=$nb_fname --to python $nb_fname')
    # nb_fname要當作變數帶入檔名，要加$
    # 轉檔後生成nb_fname.py
except:
    pass


# In[ ]:




