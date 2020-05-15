
# coding: utf-8
---
title: "Beautiful Soup Basic HTML Scraping"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Beautiful soup basic HTML scraping."
type: technical_note
draft: false
---
# ### Import the modules

# In[79]:


# Import required modules
import requests
from bs4 import BeautifulSoup


# ### Scrap the html and turn into a beautiful soup object

# In[80]:


# Create a variable with the url
url = 'http://chrisralbon.com'

# Use requests to get the contents
r = requests.get(url)

# Get the text of the contents
html_content = r.text

# Convert the html content into a beautiful soup object
soup = BeautifulSoup(html_content, 'lxml')


# ### Select the website's title

# In[81]:


# View the title tag of the soup object
soup.title


# ### Website title tag's string

# In[82]:


# View the string within the title tag
soup.title.string


# ### First paragraph tag

# In[83]:


# view the paragraph tag of the soup
soup.p


# ### The parent of the title tag

# In[84]:


soup.title.parent.name


# ### The first link tag

# In[85]:


soup.a


# ### Find all the link tags and list the first five

# In[86]:


soup.find_all('a')[0:5]


# ### The string inside the first paragraph tag

# In[87]:


soup.p.string


# ### Find all the h2 tags and list the first five

# In[88]:


soup.find_all('h2')[0:5]


# ### Find all the links on the page and list the first five

# In[89]:


soup.find_all('a')[0:5]

