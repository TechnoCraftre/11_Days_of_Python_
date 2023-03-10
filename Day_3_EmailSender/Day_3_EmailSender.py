#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib

to = input("Enter the email of recipient: \n")

content = input("Enter the content for mail: \n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
#please enter the correct gmail credentials to login the account
#the email and password entered are sample
    server.login("senderemail@gmail.com", "12345")
    server.sendmail("senderemail@gmail.com", to, content)
    server.close()
sendEmail(to, content)

