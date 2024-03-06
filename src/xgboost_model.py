#!/usr/bin/env python
# coding: utf-8

# # Importing the dataset

# In[80]:


import pandas as pd


# In[81]:


df=pd.read_csv("preprocessed_data.csv")


# In[82]:


df.head()


# # Preprocessing

# In[83]:


df=df.set_index('ENCNTR_ID')


# In[84]:


df.head()


# # Building the model (XGBoost)

# ### Importing the nesscary libraries

# In[90]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import json
import joblib


# ### Data (new randomized data) to test that the model works

# In[88]:


new_data=pd.DataFrame({'FACILITY':['KFSH&RC Riyadh'],
                       'BUILDING':['EMS'],
                       'ADMIT_MODE':['Wheelchair'],
                       'DAY_OF_WEEK':['Thursday'],
                       'AGE':[71]
})


# # Loop for each acuity level model

# In[91]:


acuity_levels=df['ACUITY_LEVEL'].unique()

for acuity_level in acuity_levels:
    df_acuity=df[df['ACUITY_LEVEL']==acuity_level].copy()
    print(f"Acuity Level: {acuity_level}")
    df_acuity.drop('ACUITY_LEVEL', inplace=True, axis=1)

    label_encoder=LabelEncoder()
    df_acuity['FACILITY']=label_encoder.fit_transform(df_acuity['FACILITY'])
    df_acuity['BUILDING']=label_encoder.fit_transform(df_acuity['BUILDING'])
    df_acuity['ADMIT_MODE']=label_encoder.fit_transform(df_acuity['ADMIT_MODE'])
    df_acuity['DAY_OF_WEEK']=label_encoder.fit_transform(df_acuity['DAY_OF_WEEK'])

    X = df_acuity.drop(columns=['WAITING_TIME_IN_MIN'])
    y = df_acuity['WAITING_TIME_IN_MIN']

    X_train , X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model=XGBRegressor()
    
    param_grid={'n_estimators': [100,200,300],
             'learning_rate':[0.01,0.1,0.2],
             'max_depth': [3, 5, 7],
             'subsample': [0.8, 1.0],
             'colsample_bytree': [0.8, 1.0]
    }
    
    grid_search = GridSearchCV(estimator=model,
                        param_grid=param_grid,
                           scoring='neg_mean_absolute_error',
                          cv=5)
    
    grid_search.fit(X_train, y_train)

    best_model=grid_search.best_estimator_

    joblib.dump(best_model, f'xgboost_{acuity_level}.joblib')
    
    y_pred=best_model.predict(X_test)

    mse=mean_squared_error(y_test, y_pred)
    print("Mean squared error: ", mse)
    mae=mean_absolute_error(y_test, y_pred)
    print("Mean squared erroe: ", mae)

    new_data['FACILITY']=label_encoder.fit_transform(new_data['FACILITY'])
    new_data['BUILDING']=label_encoder.fit_transform(new_data['BUILDING'])
    new_data['ADMIT_MODE']=label_encoder.fit_transform(new_data['ADMIT_MODE'])
    new_data['DAY_OF_WEEK']=label_encoder.fit_transform(new_data['DAY_OF_WEEK'])

    new_features=new_data[['FACILITY','BUILDING','ADMIT_MODE','DAY_OF_WEEK','AGE']]

    new_prediction=best_model.predict(new_features)
    print(new_prediction)
    
    print("---------------------------------------------------------------------------")

