#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("C:\weekly_call_data\weekdata*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)


# In[87]:


all_data.head()


# In[ ]:




