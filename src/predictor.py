#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_prediction(model, processed_data):
    predictions=model.predict(processed_data)
    predictions=predictions.round().astype('int')
    print("The waiting time in minutes:", predictions)
    return predictions

