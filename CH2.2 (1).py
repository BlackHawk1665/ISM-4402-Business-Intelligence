#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
from sqlalchemy import create_engine

db_file = r'C:\gradedata.db' 
engine = create_engine(r"sqlite:///{}".format(db_file)) 
sql = 'SELECT * from test where Grades in (76,77,78)' 
grade_data_df = pd.read_sql(sql, engine) 
grade_data_df


# In[35]:





# In[ ]:




