#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('transaction.csv')


# In[3]:


data = pd.read_csv('transaction.csv',sep=';')


# In[ ]:


#Summary of Data


# In[ ]:


#Working with Calculations
#Defining Variables


# In[4]:


CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6


# In[ ]:


#Mathematical Operations


# In[5]:


ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransaction = NumberofItemsPurchased*CostPerItem
SellingPricePerTransaction = NumberofItemsPurchased*SellingPricePerItem


# In[ ]:


#CostPerTransaction Column Calculation


# In[6]:


CostPerItem = data['CostPerItem']


# In[7]:


NumberofItemsPurchased = data['NumberOfItemsPurchased']


# In[8]:


CostPerTransaction = CostPerItem * NumberofItemsPurchased


# In[ ]:


#Adding new column to dataframe


# In[9]:


data['CostPerTransaction'] = CostPerTransaction


# In[ ]:


#SalesPerTransaction


# In[10]:


data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']


# In[ ]:


#Profit Calculation
#Sales-Cost


# In[11]:


data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']


# In[ ]:


#Markup = sales-cost/cost


# In[12]:


data['Markup'] = ( data['SalesPerTransaction'] - data['CostPerTransaction'])/ data['CostPerTransaction']


# In[ ]:


#Rounding Markup


# In[13]:


roundmarkup = round(data['Markup'], 2)


# In[14]:


data['Markup'] = round(data['Markup'], 2)


# In[ ]:


#Combining data fields


# In[36]:


data['date'] = data['Day'].astype(str) + '-' + data['Month'] + '-' + data['Year'].astype(str)


# In[ ]:


#Using split to split client keyword field


# In[38]:


split_col = data['ClientKeywords'].str.split(',' , expand=True)


# In[ ]:


#creating new columns for client keywords


# In[39]:


data['ClientAge'] = split_col[0]


# In[40]:


data['clientType'] = split_col[1]


# In[41]:


data['LengthofContract'] = split_col[2]


# In[ ]:


#Using replace function


# In[49]:


data['ClientAge'] = data['ClientAge'].str.replace('[' , '')


# In[50]:


data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')


# In[ ]:


#Changing items to lowercase


# In[51]:


data['ItemDescription'] = data['ItemDescription'].str.lower()


# In[ ]:


#Merging files, bringing in a new dataset


# In[53]:


seasons = pd.read_csv('value_inc_seasons.csv', sep=';')


# In[54]:


data = pd.merge(data, seasons, on = 'Month')


# In[ ]:


#Dropping Columns


# In[57]:


data = data.drop('ClientKeywords', axis = 1)


# In[59]:


data = data.drop(['Day', 'Month', 'Year'], axis = 1)


# In[ ]:


#Export into csv


# In[61]:


data.to_csv('ValueInc_Cleaned.csv', index = False)


# In[ ]:




