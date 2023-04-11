#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pyshorteners

url = input("Enter the URL to shorten: \n")

print("The URL after shortening is : ", pyshorteners.Shortener().tinyurl.short(url))


# In[ ]:




