#!/usr/bin/env python
# coding: utf-8

# # Part 1: Decision Trees

# ### Import Packages & Load Dataset

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# In[2]:


Titanic = sns.load_dataset('titanic')


# ### Renaming column name which is a keyword

# In[3]:


Titanic.rename(columns={'class': 'classification'}, inplace=True)
Titanic.head()


# ### Data Wrangling: Recoding strings to numerals

# In[4]:


def Classification (series): 

    if series == "First":
        return 1

    if series == "Second": 
        return 2
    
    if series == "Third": 
        return 3

Titanic['classificationR'] = Titanic['classification'].apply(Classification)


# In[5]:


def Deck (series):

    if series == "A":
        return 1

    if series == "B": 
        return 2

    if series == "C": 
        return 3

    if series == "D": 
        return 4
    
    if series == "E":
        return 5
    
    if series == "F":
        return 6
    
    if series == "G":
        return 7

Titanic['deckR'] = Titanic['deck'].apply(Deck)


# In[15]:


def Adult_male (series): 

    if series == True:
        return int(True)

    if series == False: 
        return int(False)

Titanic['adult_maleR'] = Titanic['adult_male'].apply(Adult_male)


# In[20]:


def Embarked (series): 

    if series == "S":
        return 1

    if series == "C": 
        return 2
    
    if series == "Q": 
        return 3

Titanic['embarkedR'] = Titanic['embarked'].apply(Embarked)


# In[21]:


def Sex (series): 

    if series == "male":
        return 1

    if series == "female": 
        return 2

Titanic['sexR'] = Titanic['sex'].apply(Sex)


# In[16]:


Titanic.head()


# ### Delete rows with missing data

# In[22]:


Titanic1=Titanic.dropna(axis=0, how='any', inplace=False)


# In[23]:


Titanic1.head()


# ### Subsetting variables into arrays

# In[24]:


x = Titanic1[['pclass', 'age', 'sibsp', 'parch', 'fare', 'embarkedR','classificationR', 'adult_maleR', 'deckR','sexR']]
y = Titanic1['survived']


# ### Train-test split

# In[32]:


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=101)


# ### Initial Decision Tree

# In[33]:


decisionTree = DecisionTreeClassifier(random_state=101)
decisionTree.fit(x_train, y_train)


# ### Assessing Model Predicition

# In[37]:


treePredictions = decisionTree.predict(x_test)
print(confusion_matrix(y_test, treePredictions))


# In[38]:


print (classification_report(y_test, treePredictions))


# In[ ]:





# # Part 2: Random Forests

# ### Import package

# In[40]:


from sklearn.ensemble import RandomForestClassifier


# ### Initial Random Forest Model

# In[41]:


forest = RandomForestClassifier(n_estimators=500, random_state=101)
forest.fit(x_train, y_train)


# ### Assessing model predictions

# In[42]:


forestPredictions = forest.predict(x_test)
print(confusion_matrix(y_test, forestPredictions))


# In[43]:


print(classification_report(y_test, forestPredictions))


# In[ ]:




