#!/usr/bin/env python
# coding: utf-8

# # Examining Mrs. Dalloway with NLTK
# 
# <!-- This code uses Python's NLTK module to explore a copy of the novel Mrs. Dalloway.  -->

# In[1]:


import pandas as pd 
import numpy as np
import nltk
import unittest

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords

nltk.download('punkt')


# In[2]:


###### Category 2: Utilize External Data
#   * Read data from an external file, such as text, JSON, CSV, etc, and use that data in your application.

# This program uses the external file "mrs.dalloway.txt" to call up a text version of _Mrs. Dalloway_. You can find this code in cell 3. The text file is later converted and manipulated to reveal data about _Mrs. Dalloway_. 


# In[3]:


f = open('mrs_dalloway.txt', 'r')
mrs_dalloway = f.read()
print(mrs_dalloway)


# In[4]:


###### Category 1: Python Programming Basics
#   * Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.
#   * Implement a regular expression (regex)
  
# This program turns the mrs.dalloway.txt file into a list of individual words using regexp code with the NLTK tokenizer, found in cell 5. The list of indidvidual words is later visualized, dissected, and tested. 
# The code also uses a regexp line of code to turn the text from one long string to individual strings.


# In[5]:


tokenizer = nltk.RegexpTokenizer(r"\w+")
new_dalloway_words = tokenizer.tokenize(mrs_dalloway)

print(new_dalloway_words)


# In[6]:


text_dalloway_for_data = nltk.Text(new_dalloway_words)
text_dalloway_for_data


# In[7]:


###### Category 3: Data Display
#   * Visualize data in a graph, chart, or other representation
  
#  This program visualizes how often certain words appear within the _Mrs. Dalloway_ text, using a lexical dispersion plot. 
#  You can change the words that appear in the plot by changing the words within the list in cell 8.


# In[8]:


text_dalloway_for_data.dispersion_plot(
    ['woman', 'ladies', 'market', 'gentleman', 'manners', 'public', 'party']
)


# In[9]:


dalloway_distribution = FreqDist(text_dalloway_for_data)
print(dalloway_distribution)


# In[10]:


nltk.download('stopwords')


stop_words = set(stopwords.words('english'))

stop_words


# In[11]:


dalloway_no_stop_words = [word for word in text_dalloway_for_data if word.casefold() not in stop_words]
dalloway_no_stop_words


# In[12]:


dalloway_distribution = FreqDist(dalloway_no_stop_words)
dalloway_distribution.most_common(10)


# In[13]:


text_dalloway_for_data.collocations(num=1)=="Peter Walsh"


# In[14]:


###### Category 4: Best Practices
#   * Create 3 or more unit tests for your application.
  
#  This code uses three unit tests to check the functionality of previous code, or whether certain text appears within the _Mrs. Dalloway_ text. 
#  You can find it within cell 15.


# In[15]:


class TestDallowayText(unittest.TestCase):
    def test_check_most_frequent_word(self):
        pull_number = dalloway_distribution.most_common(10)
        self.assertEqual(pull_number[1][1], 410)
        
# This tests whether the specified value from the dalloway_distribution list of tuples matches the second value.
        
    def test_word_search(self):
        sentence = "What a lark!"
        self.assertIn(sentence, mrs_dalloway)

# This tests whether the 'sentence' string matches any text within the _Mrs. Dalloway_ file.

    def test_stop_word_actually_removed(self):
        stop_word_single = [stop_word for stop_word in stop_words]
        self.assertIn(stop_word_single, dalloway_no_stop_words)
        
# This tests whether all the stop words were actually removed from the text_dalloway_for_data data set back in cell 11.

unittest.main(argv=[''], verbosity=2, exit=False)

