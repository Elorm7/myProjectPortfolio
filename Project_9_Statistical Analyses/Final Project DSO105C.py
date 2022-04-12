#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import scipy
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.proportion import proportions_chisquare


# ## Scenario 1 - One proportion z-test

# In[3]:


count = 28
nobs = 94
value = .16
stat, pval = proportions_ztest(count, nobs, value)
print(stat,pval)


# #### CONCLUSION: The number of fraudulent claims is significantly different (higher) than the reported industry average

# ## Scenario 2 - Independent Chi-Square

# In[4]:


antiseptics = pd.read_csv("C:/Users/Richmond/Desktop/WOZ-U/Intermediate Statistics/Final Project/antiseptics.csv")
antiseptics.head()


# In[5]:


antiseptics.rename(columns={'Antiseptic Type ': "AS", "Number of applications": "Count"}, inplace=True)


# In[6]:


antiseptics.head()


# In[7]:


pivot = pd.pivot_table(antiseptics,index='AS',columns='Clinic',values="Count")
pivot


# In[9]:


stats.chi2_contingency(pivot)


# #### CONCLUSION: There is no significant difference in the ratios of the various antiseptic types being used by the clinics

# ## Scenario 3 - One Way ANOVA

# In[10]:


savings = pd.read_csv("C:/Users/Richmond/Desktop/WOZ-U/Intermediate Statistics/Final Project/savings.csv")
savings.head()


# In[22]:


savings1 = pd.melt(savings,var_name='Group', value_name='Amount')
savings1.head()


# In[23]:


savings1 = savings1.replace(savings.columns, [0,1,2,3])
savings1.head()


# ### Check for Normality

# In[24]:


sns.distplot(savings1.Amount)


# In[25]:


#Normaally distributed


# ### Testing Homogeneity of Variance

# In[28]:


scipy.stats.bartlett(savings1["Amount"], savings1["Group"])


# In[29]:


#Assumption failed, so we proceed with caution


# In[30]:


#Drop missing values permanently

savings1.dropna(inplace = True)


# ### Running Analysis

# In[31]:


stats.f_oneway(savings1['Amount'][savings1['Group']== 0],
              savings1['Amount'][savings1['Group']== 1],
              savings1['Amount'][savings1['Group']== 2],
              savings1['Amount'][savings1['Group']== 3])


# #### CONCLUSION: There exists significant differences in the saving practices of the various demographic groups

# ## Scenario 4 - Two proportion z-test

# In[51]:


# Summary of Data

# School age children total: 503
#       favored: 374
#  not in favor: 119

# Without sch age children total: 245
#        favored: 171
#  not in favour: 74


# In[53]:


count = np.array([374, 171])
nobs = np.array([503, 245])
stat, pval = proportions_ztest(count, nobs)
print(stat,pval)


# #### CONCLUSION: There are no significant differences in the sentiments expressed via the polls based on demographic groups.
