#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "C:/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


import numpy as np
df['TimeMgmt'] = np.where((df['hours']>17) & (df['exercise']>3),'Busy', 'NotBusy')
df.head(10)


# In[ ]:




