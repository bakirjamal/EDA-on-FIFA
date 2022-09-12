#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


fifa=pd.read_csv("players_20.csv")


# In[3]:


fifa.head()


# In[4]:


fifa.shape


# In[5]:


for col in fifa.columns:
    print(col)
    


# In[6]:


18483*106


# In[7]:


fifa["nationality"].value_counts()


# In[8]:


fifa["nationality"].value_counts()[0:10]


# In[9]:


fifa["nationality"].value_counts()[0:5]


# In[10]:


fifa["nationality"].value_counts()[0:5].keys()


# In[11]:


plt.figure(figsize=(5,7))
plt.bar(list(fifa["nationality"].value_counts()[0:5].keys()),list(fifa["nationality"].value_counts()[0:5]),color=["red","yellow","pink","orange","black"])
plt.show()


# In[12]:


player_salary=fifa[["short_name","wage_eur"]]


# In[13]:


player_salary.head()


# In[14]:


player_salary.value_counts()


# In[15]:


player_salary.value_counts()[0:10]


# In[16]:


player_salary=player_salary.sort_values(by=["wage_eur"],ascending=False)


# In[17]:


plt.figure(figsize=(8,5))
plt.bar(list(player_salary["short_name"][0:5]),list(player_salary["wage_eur"][0:5]),color=["red","yellow","pink","black","blue"])
plt.title("MOST PAID PLAYER")
plt.xlabel("player name")
plt.ylabel("SALARY IN EUR")
plt.grid()
plt.show()


# In[18]:


fifa["nationality"]=="Germany"


# In[19]:


Germany=fifa[fifa["nationality"]=="Germany"]
Germany.head(10)


# In[20]:


Germany.sort_values(by=["height_cm"],ascending=False).head()


# In[21]:


Germany.sort_values(by=["weight_kg"],ascending=False).head()


# In[22]:


Germany.sort_values(by=["wage_eur"],ascending=False).head()


# In[23]:


Germany[["short_name","wage_eur"]].sort_values(by=["wage_eur"],ascending=False).head(10)


# In[24]:


player_shooting=fifa[["short_name","shooting"]]


# In[25]:


player_shooting.head(10)


# In[26]:


player_shooting.sort_values(by=["shooting"],ascending=False).head(10)


# In[27]:


player_defending= fifa[["short_name","defending","nationality","club_name"]]


# In[28]:


player_defending.sort_values(by=["defending"],ascending=False).head(10)


# In[29]:


real_madrid=fifa[fifa["club_name"]=="Real Madrid"]


# In[30]:


real_madrid.sort_values(by=["wage_eur"],ascending=False).head()


# In[31]:


real_madrid.sort_values(by=["shooting"],ascending=False).head()


# In[32]:


real_madrid.sort_values(by=["defending"],ascending=False).head()


# In[33]:


real_madrid["nationality"].value_counts()


# In[ ]:




