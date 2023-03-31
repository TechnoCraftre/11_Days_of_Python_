#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import webbrowser as wb
def webauto():
    chrome_path = "C:\Program Files\Google\Chrome\Application"
    URLS = (
        "https://www.youtube.com/",
        "https://stackoverflow.com/",
        "https://github.com/"
    )
    for url in URLS:
        print("Opening: "+ url)
        wb.get(chrome_path).url
webauto()


# In[ ]:




