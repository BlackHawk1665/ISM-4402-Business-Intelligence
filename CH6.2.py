#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
Location = "C:/gradedata.csv"
df = pd.read_csv(Location)
df.head()
df.corr()


# In[19]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ exercise + hours + gender',data=df).fit()
result.summary()


# In[ ]:




