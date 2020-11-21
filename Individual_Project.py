#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
Location = "C:/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[20]:


pd.pivot_table(df,
               values=['Cars Sold'],
               index=['Hours Worked'],
               margins='True')


# In[5]:


import pandas as pd
Location = "C:/axisdata.csv"
df = pd.read_csv(Location)
maximum_values = pd.DataFrame(columns=['Cars Sold'])
for v in list(df.columns.values):
    maximum_values.loc[v] = [df[v].max()]
maximum_values


# In[6]:


minimum_values = pd.DataFrame(columns=['Minimum Values'])
for v in list(df.columns.values):
    minimum_values.loc[v] = [df[v].min()]
minimum_values


# In[7]:


pd.pivot_table(df,
               values=['Cars Sold'],
               index=['Gender'])


# In[21]:


df2 = df.loc[df['Cars Sold'] >= 3]
pd.pivot_table(df2,values=['Hours Worked'],index=['Cars Sold'],margins='True')


# In[16]:


df['Years Experience'].mean()


# In[22]:


df2 = df.loc[df['Cars Sold'] >= 3]
pd.pivot_table(df2,values=['Years Experience'],index=['Cars Sold'],margins='True')


# In[19]:


pd.pivot_table(df,values=['Cars Sold'],index=['SalesTraining'])


# In[41]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:/axisdata.csv"
df = pd.read_csv(Location)
df.hist(column="Cars Sold", by="Gender")


# In[42]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:/axisdata.csv"
df = pd.read_csv(Location)
df.hist(column="Cars Sold", by="SalesTraining")


# In[ ]:




