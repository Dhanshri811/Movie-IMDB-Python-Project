#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[8]:


import matplotlib.pyplot as plt


# In[5]:


import seaborn as sns


# In[6]:


df = pd.read_csv(r'/home/nineleaps/Documents/IMDB-Movie-Data.csv')


# In[7]:


df.head()


# In[10]:


df.shape


# In[11]:


print('Number of rows:', df.shape[0])
print('Number of columns:', df.shape[1])


# In[13]:


df.info()


# In[20]:


print('Any missing values?', df.isnull().values.any())


# In[22]:


df.isnull().sum()


# ## Missing values by Heatmap

# In[23]:


sns.heatmap(df.isnull())


# # Dropping a unnamed column which has maximum null values

# In[27]:


df1= df.drop(df.columns[12], axis=1)


# In[28]:


df1.head()


# In[31]:


percentage_missing = df1.isnull().sum()*100/len(df1)
percentage_missing


# ## Dropping the rows of null values

# In[33]:


df1.dropna(axis=0, inplace= True)


# In[36]:


percentage_missing_new = df1.isnull().sum()*100/len(df1)
percentage_missing_new


# In[37]:


df1.shape


# ## Check for duplicate values 

# In[41]:


dup_value = df1.duplicated().any()


# In[42]:


print('Are there any dupliacted value in dataset?', dup_value)


# In[ ]:


df1.drop_duplicated() # If there is any duplicated value then 

df['Revenue']= df['Revenue'].fillna(df['Revenue'].mean()) #If i want to fill that null values with mean of the column then,


# In[50]:


df1.describe(include= 'all')


# In[ ]:





# In[ ]:




