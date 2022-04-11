#!/usr/bin/env python
# coding: utf-8

# ## Lesson One HandsOn_ML

# ### Importing packages

# In[62]:


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn import metrics
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


# ### Importing 'Diamonds' dataset

# In[63]:


diamonds = pd.read_csv ('C:/Users/Richmond/Desktop/WOZ-U/Machine Learning/HandsOn/ML repo/Diamonds.csv')
print (diamonds)


# ### Recoding Cut to CutR

# In[64]:


def Cut (series): 

    if series == "Ideal":
        return 5

    if series == "Premium": 
        return 4

    if series == "Very Good": 
        return 3

    if series == "Good": 
        return 2
    
    if series == "Fair":
        return 1
    

diamonds['cutR'] = diamonds['cut'].apply(Cut)


# ### Recoding Color to ColorR

# In[66]:


def Color (series): 

    if series == "D":
        return 7

    if series == "E": 
        return 6

    if series == "F": 
        return 5

    if series == "G": 
        return 4
    
    if series == "H":
        return 3
    
    if series == "I":
        return 2
    
    if series == "J":
        return 1
    

diamonds['colorR'] = diamonds['color'].apply(Color)


# ### Recoding Clarity to ClarityR

# In[67]:


def Clarity (series): 

    if series == "I1":
        return 1

    if series == "SI2": 
        return 2

    if series == "SI1": 
        return 3

    if series == "VS2": 
        return 4
    
    if series == "VS1":
        return 5
    
    if series == "VVS2":
        return 6
    
    if series == "VVS1":
        return 7
    
    if series == "IF":
        return 8
    

diamonds['clarityR'] = diamonds['clarity'].apply(Clarity)


# ### Dataset with new columns: cutR, colorR, clarityR 

# In[68]:


print(diamonds)


# ### Creating X and Y variables (subsetting into arrays)

# In[77]:


x = diamonds[['carat', 'cutR', 'colorR', 'clarityR']]
y = diamonds['price']


# ### Train-test split: 60/40

# In[96]:


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = .4, random_state=101)


# ### Data shape (rows, columns)

# In[97]:


print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)


# ### Linear Regression Model

# In[98]:


lm = LinearRegression()
lm.fit(x_train, y_train)


# In[99]:


predictions = lm.predict(x_test)
predictions


# ### Scatter plot of model predictions

# In[100]:


plt.scatter(y_test, predictions)


# ### Model Accuracy Score

# In[101]:


print("Score:", lm.score(x_test, y_test))

#The model predictions are accurate about 90% of the time.


# ### Root Mean Squared Error

# In[102]:


np.sqrt(metrics.mean_squared_error(y_test, predictions))


# ### Cross Validation

# In[113]:


print(cross_val_score(lm, x,y, cv=5))


# In[114]:


accuracy = cross_val_score(lm, x,y, cv=5)
print(accuracy)
print("Accuracy of Model with Cross Validation is:", accuracy.mean() * 100)


# In[ ]:




