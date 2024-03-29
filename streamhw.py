#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install matplotlib


# In[2]:


import streamlit as st
import pandas as pd
import numpy as np



# In[3]:


df = pd.read_csv('jobs_in_data.csv')


# In[4]:


df.head()


# In[5]:


df.shape


# In[6]:


st.title('Jobs and Salaries in Data Science')
st.markdown("This dashboard shows some information about work and salary in the context of the job category in the Data Science")


# In[7]:


st.dataframe(df)


# In[8]:


profession = list(df['job_category'].unique())


# In[9]:


st.header("Choose a job category")
status = st.radio('category:', profession)


# In[10]:


statistics = pd.DataFrame(round(df[df['job_category'] == status].groupby('work_year').describe()['salary_in_usd']))
st.header(f'Descriptive statistics of salary in USD in {status}')
st.dataframe(statistics)


# In[11]:


grade = pd.DataFrame(df[df['job_category'] == status].groupby(['work_year', 'experience_level']).size().unstack(fill_value=0))
st.header(f'Number of employees by qualification levels and year in {status}')
st.dataframe(grade)


# In[12]:


grade = pd.DataFrame(grade.reset_index())


# In[13]:

try:
    st.line_chart(
       grade, x="work_year", y=["Entry-level", "Executive", "Mid-level", "Senior"]
)
except Exception:
   print('You can not build a graph based on the data')

# In[14]:


working_conditions = pd.DataFrame(df[df['job_category'] == status].groupby(['work_year', 'work_setting']).size().unstack(fill_value=0))
st.header(f'Number of employees by working conditions and year in {status}')
st.dataframe(working_conditions)


# In[15]:


working_conditions = pd.DataFrame(working_conditions.reset_index())


# In[16]:

try:
    st.line_chart(
       working_conditions, x="work_year", y=["Hybrid", "In-person", "Remote"]
)
except Exception:
    print('You can not build a graph based on the data')


