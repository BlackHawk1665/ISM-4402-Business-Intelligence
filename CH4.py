#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
Location = "C:/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[22]:


bins = [0,60,70,80,90,100]
group_names = ['Fail', 'Fail', 'Pass', 'Pass', 'Pass']


# In[23]:


df['letterGrades'] = pd.cut(df['grade'],bins, labels=group_names)
df.head()


# In[ ]:




