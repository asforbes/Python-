#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[2]:


import numpy as np


# In[102]:


import matplotlib.pyplot as plt


# In[3]:


with open("loan_data_json.json") as f:
        data = json.load(f)


# In[4]:


#Transform to DataFrame


# In[ ]:


for i in range(0, len(data)):
    print(data[i])


# In[19]:


import pandas as pd
df = pd.DataFrame(columns=["credit.policy", "purpose", "int.rate", "installment", "log.annual.inc", "dti", "fico", "days.with.cr.line", "revol.bal", "revol.util", "inq.last.6mths", "delinq.2yrs", "pub.rec", "not.fully.paid"])


# In[27]:


for i in range(0, len(data)):
    currentItem = data[i]
    df.loc[i] = [data[i]["credit.policy"], data[i]["purpose"], data[i]["int.rate"], data[i]["installment"], data[i]["log.annual.inc"], data[i]["dti"], data[i]["fico"], data[i]["days.with.cr.line"], data[i]["revol.bal"], data[i]["revol.util"], data[i]["inq.last.6mths"], data[i]["delinq.2yrs"], data[i]["pub.rec"], data[i]["not.fully.paid"]]


# In[ ]:


# Description of Data 


# In[ ]:


df['int.rate'].describe()


# In[ ]:


df['fico'].describe()


# In[ ]:


df['dti'].describe()


# In[ ]:


# Using EXP to get annual income 


# In[122]:


income = np.exp(df['log.annual.inc'])


# In[ ]:


df['log.annual.inc'] = income


# In[ ]:


# If Statements


# In[ ]:


#FICO Score


# In[64]:


fico = 515


# In[65]:


#fico >= 300 and < 400: 'Very Poor'
#fico >= 400 and ficoscore < 600: 'Poor'
#fico >= 601 and ficoscore < 660:'Fair'
#fico >= 660 and ficoscore < 780:'Good'
#fico >= 780:'Excellent'


# In[ ]:


if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    ficocat = 'Good'
elif fico >= 700 :
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)


# In[ ]:


# Applying for loops to loan data(df)
#using the first ten


# In[73]:


length = len(df)


# In[87]:


ficocat = []


# In[89]:


for x in range(0,length):
    category = df['fico'][x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400  and category < 600:
        cat = 'Poor'
    elif category >= 601 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 700:
        cat = 'Good'
    elif category >= 700:
        cat = 'Excellent'
    else:
        cat = 'Unknown'
    ficocat.append(cat)


# In[90]:


ficocat = pd.Series(ficocat)


# In[91]:


df['fico.category'] = ficocat


# In[ ]:


length = len(df)


# In[ ]:


ficocat = []


# In[ ]:


#df.loc as conditional statements 


# In[ ]:


# df.loc[df[columnname] condition, newcolumnname] = 'value if the condition is met'


# In[ ]:


#for interest rates, a new column is wanted, rate >0.12 then high, else low


# In[98]:


df.loc[df['int.rate'] >0.12, 'int.rate.type'] = 'high'


# In[99]:


df.loc[df['int.rate'] <= 0.12, 'int.rate.type'] = 'low'


# In[ ]:


# Number of loans/rows by fico.category


# In[ ]:


catplot = df.groupby(['fico.category']).size()
catplot.plot.bar(color = 'red', width = 0.3)
plt.show()


# In[ ]:


purposecount = df.groupby(['purpose']).size()
purposecount.plot.bar(color = 'green', width = 0.3)
plt.show()


# In[ ]:


#Scatter Plots 


# In[ ]:


ypoint = df['log.annual.inc']
xpoint = df['dti']
plt.scatter(xpoint, ypoint)
plt.show()


# In[ ]:


#Writing to csv


# In[129]:


df.to_csv('df.cleaned.csv', index = True)


# In[ ]:




