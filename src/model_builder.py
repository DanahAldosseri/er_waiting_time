#!/usr/bin/env python
# coding: utf-8

# In[1]:


import joblib


# In[2]:


def load_model(acuity_level):
    model_filename=rf'xgboost_{acuity_level}.joblib'
    loaded_model=joblib.load(model_filename)
    return loaded_model

