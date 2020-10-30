#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
Location = "C:\gradedata.csv"
df = pd.read_csv(Location)
get_ipython().run_line_magic('matplotlib', 'inline')
dataframe = pd.read_csv(Location)
plt.scatter(dataframe['hours'], dataframe['grade'])


# In[17]:


df.head()


# In[ ]:




