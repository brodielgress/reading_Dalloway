# Reading Mrs. Dalloway with the NLTK module
My project for the Python - Data Analysis Course 2

by Brodie Gress

## About

This project uses the NLTK module from Python to explore the language used within _Mrs. Dalloway_, by Virginia Woolf. 

## Requirements

Python 3 and Jupyter Notebook are required to run this program. If you need, [update or download Python here](https://www.python.org).

Open the code on Jupyter Notebook to explore a few insights into this classic text. Please install the following packages before you run the program:

1. pandas as pd 
2. numpy as np
3. nltk
4. unittest

5. from nltk.tokenize import sent_tokenize, word_tokenize
6. from nltk import FreqDist
7. from nltk.corpus import stopwords

## Code Louisville Requirements

Below, I explain how my project meets the Code Louisville requirements. You can also find these categories listed above their respective cells.

###### Category 1: Python Programming Basics
  * Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.
  * Implement a regular expression (regex)
  
This program turns the mrs.dalloway.txt file into a list of individual words using regexp code with the NLTK tokenizer, found in cell 5. The list of indidvidual words is later visualized, dissected, and tested. The code also uses a regexp line of code to turn the text from one long string to individual strings.

###### Category 2: Utilize External Data
  * Read data from an external file, such as text, JSON, CSV, etc, and use that data in your application.

This program uses the external file "mrs.dalloway.txt" to call up a text version of _Mrs. Dalloway_. You can find this code in cell 3. The text file is later converted and manipulated to reveal data about _Mrs. Dalloway_. 

###### Category 3: Data Display
  * Visualize data in a graph, chart, or other representation
  
This program visualizes how often certain words appear within the _Mrs. Dalloway_ text, using a lexical dispersion plot. 
You can change the words that appear in the plot by changing the words within the list in cell 8.


###### Category 4: Best Practices
   * Create 3 or more unit tests for your application.
  
This code uses three unit tests to check the functionality of previous code, or whether certain text appears within the _Mrs. Dalloway_ text. 
You can find it within cell 15.


## Acknowledgements

Thank you, Code Louisville, for the education and opportunities you've served me over four rounds of learning HTML, CSS, JavaScript, and Python. Thank you especially to the mentors who helped me along the way; Will, good luck in graduate school! I'd also like to thank my fellow classmates; their projects are stunning and show me I have so much more to learn about frontend web development, data analysis, and coding in general.

Code Louisville has been a wonderful nest in which to learn coding, and now I feel ready to fly on my own. Before I started, I thought coding was this inscrutable wizardry only teen prodigies or dedicated college students could understand, but coding really does boil down to understanding the logic underlying all your lines of code. If you're determined, know how to research online, and willing to try, try, and try ad infinitum, you can solve almost any problem you create in your code.

Thank you again, and I hope you enjoy my small project.
