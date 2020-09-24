#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
Location =  "C:\gradedata.csv"
df = pd.read_csv(Location)
df.loc[(df['grade'] <= 0,'grade')] = 0


# In[22]:


df.head()


# In[ ]:




