#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[57]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# In[100]:


import openpyxl


# In[2]:


#Reading Excel or xlsx files


# In[5]:


data = pd.read_excel('articles.xlsx')


# In[ ]:


#Summary of the data


# In[ ]:


data.describe()


# In[ ]:


#Summary of the columns


# In[ ]:


data.info()


# In[ ]:


#Counting the number of articles by source


# In[ ]:


#Format of groupby: df.groupby(['coulmn_to_group'])['column_to_count'].count()


# In[ ]:


data.groupby(['source_id'])['article_id'].count()


# In[ ]:


#Number of reactions by publisher


# In[ ]:


data.groupby(['source_id'])['engagement_reaction_count'].sum()


# In[ ]:


#dropping a column


# In[14]:


data = data.drop('engagement_comment_plugin_count' , axis=1)


# In[ ]:


#Creating a keyword flag


# In[32]:


keyword = 'crash'


# In[33]:


#for loop to isolate each title row


# In[ ]:


#length =len(data)


# In[34]:


#keyword_flag = []


# In[36]:


#for x in range(0,length):
    #heading = data['title'][x]
    #if keyword in heading:
        #flag = 1
    #else:
        #flag = 0
    #keyword_flag.append(flag)


# In[ ]:


#Creating a function


# In[51]:


def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)


# In[ ]:


k = keywordflag('murder')


# In[ ]:


#Creating new column in DataFrame


# In[55]:


data['keyword_flag'] = pd.Series(keywordflag)


# In[ ]:


#SentimentIntensityAnalyzer


# In[60]:


sent_int = SentimentIntensityAnalyzer()


# In[61]:


text = data['title'][15]


# In[62]:


sent = sent_int.polarity_scores(text)


# In[63]:


neg = sent['neg']


# In[64]:


pos = sent['pos']


# In[65]:


neu = sent['neu']


# In[ ]:


#for loop to extract sentiment per title


# In[68]:


title_neg_sentiment = []


# In[69]:


title_pos_sentiment = []


# In[70]:


title_neu_sentiment = []


# In[76]:


length = len(data)
for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_pos_sentiment.append(neu)


# In[88]:


title_neg_sentiment = pd.Series(title_neg_sentiment)


# In[89]:


title_pos_sentiment = pd.Series(title_pos_sentiment)


# In[90]:


title_neu_sentiment = pd.Series(title_neu_sentiment)


# In[91]:


data['title_neg_sentiment'] = title_neg_sentiment


# In[92]:


data['title_pos_sentiment'] = title_pos_sentiment


# In[93]:


data['title_neu_sentiment'] = title_neu_sentiment


# In[117]:


data.to_excel('Blog_Me_Cleaned.xlsx', index = False)


# In[ ]:




