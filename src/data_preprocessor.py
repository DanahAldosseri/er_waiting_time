#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.preprocessing import LabelEncoder


# In[3]:


def preprocess_data(data):
    acuity_level=data['ACUITY_LEVEL'].values[0]
    
    label_encoder=LabelEncoder()
    data['FACILITY']=label_encoder.fit_transform(data['FACILITY'])
    data['BUILDING']=label_encoder.fit_transform(data['BUILDING'])
    data['ADMIT_MODE']=label_encoder.fit_transform(data['ADMIT_MODE'])
    data['DAY_OF_WEEK']=label_encoder.fit_transform(data['DAY_OF_WEEK'])

    new_features=data[['FACILITY', 'BUILDING','ADMIT_MODE','DAY_OF_WEEK','AGE']]

    return new_features, acuity_level

