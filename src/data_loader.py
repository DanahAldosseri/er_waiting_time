#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


def get_data():
    data=pd.DataFrame({'FACILITY':['KFSH&RC Riyadh'],
                           'ACUITY_LEVEL':['1-Resuscitation'],
                           'BUILDING':['EMS'],
                           'ADMIT_MODE':['Wheelchair'],
                           'DAY_OF_WEEK':['Thursday'],
                           'AGE':[71]
    })
    return data

