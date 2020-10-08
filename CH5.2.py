#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bs = [1,1,0,0,1]
ms = [2,1,0,0,0]
phd = [0,1,0,0,0]
GradeList = zip(names,grades,bs,ms,phd)
df = pd.DataFrame(data=GradeList,columns=['Name','Grade','BS','MS','PhD'])
df


# In[21]:


df['Grade'].count()


# In[24]:


df['Grade'].mean()


# In[26]:


df['Grade'].std()


# In[27]:


df['Grade'].min()


# In[28]:


df['Grade'].max()


# In[29]:


df['Grade'].quantile(.25)


# In[31]:


df['Grade'].quantile(.5)


# In[32]:


df['Grade'].quantile(.75)


# In[33]:


df['Grade'].mean()


# In[34]:


df['Grade'].median()


# In[35]:


df['Grade'].mode()


# In[36]:


df.var()


# In[ ]:




