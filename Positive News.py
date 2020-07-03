#!/usr/bin/env python
# coding: utf-8

# ### IMPORT LIBRARIES

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# ### IMPORT POSITIVE WORDS FILE

# In[2]:


words=pd.read_csv("Desktop/New Folder/positivewords.txt",header=None, names="w")
words.head()


# In[3]:


#Check length
print(len(words))


# In[4]:


#Get info
words.info()


# In[5]:


type(words)


# ### IMPORT NEWS HEADLINES DATA

# In[6]:


news=pd.read_csv("Desktop/New Folder/GoodBadNews.csv")
news.head()


# In[7]:


#Get info
news.info()


# In[8]:


type(news)


# In[9]:


#Drop negative news headlines
news.drop(news[news['Majority Score'] != 1].index, inplace = True) 
#Reset indices
news.reset_index(drop=True, inplace=True)
news.head(15)


# In[10]:


#Get info
news.info()


# ### PRINT POSITIVE WORDS

# In[11]:


for i in range(len(words)):
    clause=words.loc[i,"w"]
    print(clause)


# ### PRINT ALL THE HEADLINES

# In[12]:


for j in range(len(news)):
    print(news["Title"])


# ### PRINT NUMBER OF POSITIVE WORDS PRESENT IN HEADLINES

# In[13]:


print("List of all Positive Titles:")
count= [] #This will store number of positive words found in each headline
for i in range(len(news)):
    pos_words=[] #This will store the positive words in each headline
    for j in range(len(words)):
        search=words.loc[j,"w"]
        headline=news.loc[i,"Title"]
        split_word=headline.split()
        if search in split_word:
            pos_words.append(search)
    count.append(len(pos_words))
    if len(pos_words)>0:
        print("\nFor:",headline)
        print("Words found:",pos_words)
        print("No. of words found:",len(pos_words))
print(count)


# ### VISUALIZATION

# In[14]:


from matplotlib import pyplot as plt
x = news.index
y = count
plt.bar(x, y)
plt.xlabel("Heading number")
plt.ylabel("Number of positive words")
plt.title("Positive Headings with Positive Words")
plt.show()

