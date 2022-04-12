#!/usr/bin/env python
# coding: utf-8

# # Alice in Wonderland

# ### Import packages

# In[2]:


import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Read in text from website

# In[3]:


url = 'https://www.gutenberg.org/files/11/11-h/11-h.htm'


# In[4]:


r = requests.get(url)
type(r)


# ### Convert text to soup

# In[5]:


html = r.text
soup = BeautifulSoup(html,"html.parser")
type(soup)


# ### Tokenize data

# In[6]:


text = soup.get_text()
tokenizer = RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(text)
tokens[:10]


# ### Convert to all lowercase

# In[7]:


words = []
for word in tokens:
    words.append(word.lower())
    
words[:10]


# ### Remove stopwords

# In[8]:


stopwords = nltk.corpus.stopwords.words('english')
stopwords[:5]


# In[10]:


wordsWithoutStops = []
for word in words:
    if word not in stopwords:
        wordsWithoutStops.append(word)
        
wordsWithoutStops[:10]


# ### Plot graph of top 25 highest occurring words

# In[11]:


sns.set()
frequencyDis = nltk.FreqDist(wordsWithoutStops)
frequencyDis.plot(25)


# ### Conclusion

# #### The top 5 words with the highest frequency in Alice in Wonderland are: [a, said, alice, little, one]
# #### 'Alice' is a main character in the novel

# In[ ]:




