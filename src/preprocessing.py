#!/usr/bin/env python
# coding: utf-8

# # ER Waiting Time

# ## Importing the required libraries

# In[210]:


import pandas as pd


# In[211]:


get_ipython().getoutput('pip install openpyxl')


# ### Importing the dataset

# In[212]:


df=pd.read_excel("/Users/admin1/Desktop/danah/ER_waiting_time/data/ED_Waiting_time.xlsx")


# ### Visualizing the dataset

# In[213]:


df.shape


# In[214]:


df.head()


# In[215]:


df.tail()


# In[216]:


df.describe()


# Displaying all the columns of the dataset

# In[217]:


pd.set_option('display.max_columns', None)
df.head()


# In[218]:


df.columns


# In[219]:


df.dtypes


# In[220]:


df.isnull().sum()


# In[221]:


df.nunique()


# ### Displaying the histograms of the data

# In[222]:


df.hist(figsize=(25,20))


# ## Cleaning the data

# Removing the non important features

# In[223]:


to_drop = ['MRN', 'CHECKIN_NAME', 'CHECKIN_BADGE', 'CHECKOUT_BADGE', 'CHECKOUT_NAME', 'PRIMARY_DOC_NAME', 'PRIMARY_NURSE_NAME',
           'ADMIT_SRC', 'ADMIT_TYPE', 'PRIMARY_DOC_BADGE', 'PRIMARY_NURSE_BADGE']

df.drop(to_drop, inplace=True, axis=1)


# In[224]:


df.shape


# Deleting the rows the consains null value in BIRTH_DT_TM column

# In[225]:


df = df.dropna(subset=['BIRTH_DT_TM'])


# Deleting ORDER_AS and ORIG_ORDER_DT_TM because they contains a masive amount of missing values

# In[226]:


to_drop = ['ORDER_AS', 'ORIG_ORDER_DT_TM']

df.drop(to_drop, inplace=True, axis=1)


# In[227]:


df.shape


# In[228]:


df.isnull().sum()


# Droping the rows in REG_DT_TM and BED_ASSIGN_DATE that contains null value

# In[229]:


df.dropna(subset=['REG_DT_TM'], inplace=True)


# In[230]:


df.dropna(subset=['BED_ASSIGN_DATE'], inplace=True)


# In[231]:


df.isnull().sum()


# In[232]:


df.shape


# Keeping REG_DT_TM and removing CHECKIN_DT_TM, ARRIVE_DT_TM and START_TRACKING_DT_TM because they all have the same value

# In[233]:


to_drop = ['CHECKIN_DT_TM', 'ARRIVE_DT_TM', 'START_TRACKING_DT_TM']

df.drop(to_drop, inplace=True, axis=1)


# In[234]:


df.shape


# In[235]:


df.isnull().sum()


# Droping CHECKOUT_DT_TM and DEPART_DT_TM becuse we only need the DISCHARGE_DATE

# In[236]:


df.drop(['CHECKOUT_DT_TM'], inplace=True, axis=1)
df.drop(['DEPART_DT_TM'], inplace=True, axis=1)


# In[237]:


df.shape


# In[238]:


df.isnull().sum()


# Droping BASE_LOC_DT_TM because it hass alot of missing values

# In[239]:


df.drop(['BASE_LOC_DT_TM'], inplace=True, axis=1)


# In[240]:


df.isnull().sum()


# Droping TRIAGE_DATE because the time of the triage is not important 

# In[241]:


df.drop(['TRIAGE_DATE'], inplace=True, axis=1)


# Droping rows that contains null values in REASON_FOR_VISIT

# In[242]:


df=df.dropna(subset=['REASON_FOR_VISIT'], how="any")


# In[243]:


df.isnull().sum()


# Droping DISCHARGE_DATE because it has a lot of missing values

# In[244]:


df.drop(['DISCHARGE_DATE'], inplace=True, axis=1)


# In the acuity level column treat 3- Urgent and 3-Urgent the same value

# In[245]:


df['ACUITY_LEVEL'].unique()


# In[246]:


df.loc[:, 'ACUITY_LEVEL']=df['ACUITY_LEVEL'].replace({"3- Urgent":"3-Urgent"})


# ### Removing the spaces and dashes

# In[247]:


space=df[df==" "]
space.count()


# In[248]:


dash=df[df=="-"]
dash.count()


# In[249]:


incomplete_values=df[df.isin([' ', '-'])]
incomplete_values.count()


# In ACUITY_LEVEL replacing space and dash with "Unknown" 

# In[250]:


df.loc[:, 'ACUITY_LEVEL']=df['ACUITY_LEVEL'].replace({" ":"Unknown"})
df.loc[:, 'ACUITY_LEVEL']=df['ACUITY_LEVEL'].replace({"-":"Unknown"})


# Removing some values that are not a level in ACUITY_LEVEL

# In[251]:


acuity_counts=df['ACUITY_LEVEL'].value_counts()
acuity_counts


# In[252]:


values_to_del_acuity=['Unknown', 'PP', 'Ante', 'Labor', 'OR Procedure', 'C/S', 'Obs']

acuity_mask = df['ACUITY_LEVEL'].isin(values_to_del_acuity)
df = df[~acuity_mask]


# In[253]:


acuity_counts=df['ACUITY_LEVEL'].value_counts()
acuity_counts


# In[254]:


incomplete_values=df[df.isin([' ', '-'])]
incomplete_values.count()


# Removing the row that contains a dash in REASON_FOR_VISIT

# In[255]:


df=df[df['REASON_FOR_VISIT'] != '-'].dropna()


# In[256]:


incomplete_values=df[df.isin([' ', '-'])]
incomplete_values.count()


# Droping ROOM and BED columns

# In[257]:


to_drop = ['ROOM', 'BED']

df.drop(to_drop, inplace=True, axis=1)


# Droping DISCH_DISPOSITION and DISCH_TO_LOCTN columns

# In[258]:


to_drop = ['DISCH_DISPOSITION', 'DISCH_TO_LOCTN']

df.drop(to_drop, inplace=True, axis=1)


# In[259]:


incomplete_values=df[df.isin([' ', '-'])]
incomplete_values.count()


# ## Add a column named WAITING_TIME 

# In[260]:


df['WAITING_TIME_IN_MIN']=df['BED_ASSIGN_DATE'] - df['REG_DT_TM']


# In[261]:


df['WAITING_TIME_IN_MIN'] = df['WAITING_TIME_IN_MIN'].dt.total_seconds()/60


# In[262]:


df['WAITING_TIME_IN_MIN']=df['WAITING_TIME_IN_MIN'].round().astype(int)


# In[263]:


df.head()


# In[264]:


df.shape


# ### Droping REG_DT_TM and BED_ASSIGN_DATE

# In[265]:


to_drop = ['REG_DT_TM', 'BED_ASSIGN_DATE']

df.drop(to_drop, inplace=True, axis=1)


# ## Add a column named DAY_OF_WEEK

# In[266]:


df['DAY_OF_WEEK'] = pd.to_datetime(df.index).day_name()


# In[267]:


df.head()


# ## Replacing the BIRTH_DT_TM with AGE

# In[268]:


df['BIRTH_DT_TM']=pd.to_datetime(df['BIRTH_DT_TM'])
current_date=pd.to_datetime('now')
df['AGE']=(current_date - df['BIRTH_DT_TM']).dt.days//365


# In[269]:


df.drop(columns=['BIRTH_DT_TM'], inplace=True)


# ## Droping more non important features

# In[270]:


to_drop = ['LOCATION', 'REASON_FOR_VISIT', 'ENCNTR_COMPLETE_DT_TM', 'CHECKOUT_DISPOSITION_CD_DISC',
          'TRACKING_ID', 'NURSE_UNIT']

df.drop(to_drop, inplace=True, axis=1)


# ## Feature selection
# ### Choosing the input and output

# In[271]:


features=['FACILITY', 'ACUITY_LEVEL', 'BUILDING', 'ADMIT_MODE', 'DAY_OF_WEEK', 'AGE']
target=['WAITING_TIME_IN_MIN']


# ## Saving the preprocessed data in a file

# In[272]:


df.to_csv('preprocessed_data.csv', index=False)


# In[273]:


df.dtypes

