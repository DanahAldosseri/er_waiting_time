#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# In[76]:


def get_data():
    data=pd.DataFrame({'FACILITY':['KFSH&RC Riyadh'],
                           'ACUITY_LEVEL':['1-Resuscitation'],
                           'BUILDING':['EMS'],
                           'ADMIT_MODE':['Wheelchair'],
                           'DAY_OF_WEEK':['Thursday'],
                           'AGE':[71]
    })
    return data


# In[77]:


def preprocess_data(data):
    acuity_level=data['ACUITY_LEVEL'].values[0]
    
    label_encoder=LabelEncoder()
    data['FACILITY']=label_encoder.fit_transform(data['FACILITY'])
    data['BUILDING']=label_encoder.fit_transform(data['BUILDING'])
    data['ADMIT_MODE']=label_encoder.fit_transform(data['ADMIT_MODE'])
    data['DAY_OF_WEEK']=label_encoder.fit_transform(data['DAY_OF_WEEK'])

    new_features=data[['FACILITY', 'BUILDING','ADMIT_MODE','DAY_OF_WEEK','AGE']]

    return new_features, acuity_level


# In[78]:


def load_model(acuity_level):
    model_filename=rf'c:\Users\admin1\Desktop\danah\ER_waiting_time\model\xgboost_{acuity_level}.joblib'
    loaded_model=joblib.load(model_filename)
    return loaded_model


# In[79]:


def get_prediction(model, processed_data):
    predictions=model.predict(processed_data)
    predictions=predictions.round().astype('int')
    print("The waiting time in minutes:", predictions)
    return predictions


# In[80]:


def main():
    data=get_data()
    
    processed_data, acuity_level=preprocess_data(data)
    
    model=load_model(acuity_level)
    
    prediction=get_prediction(model, processed_data)


# In[81]:


if __name__ == "__main__":
    main()

