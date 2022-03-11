#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt')


# In[16]:


f = open('mrs_dalloway.txt', 'r')
mrs_dalloway = f.read()
print(mrs_dalloway)


# In[17]:


sent_tokenize(mrs_dalloway)

