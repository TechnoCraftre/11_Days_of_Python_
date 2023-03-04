#!/usr/bin/env python
# coding: utf-8

# In[1]:


""" Creating an app for screenshot capture"""

#Importing all the necessary libraries

import time
import pyautogui
from tkinter import *

#defining function screenshot

def screenshot():
    name = int(round(time.time() * 100))
    name = "{}.png".format(name)
    img = pyautogui.screenshot(name)
    img.show()

#describing the frame dimensions 

root = Tk()
root.geometry("200x200")

# Button for Screenshot
scr_button = Button(root, text="Capture Screenshoot", command=screenshot)
scr_button.pack(pady=20)
  
# Button for closing
exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=20)


root.mainloop()
exit(0)
    

