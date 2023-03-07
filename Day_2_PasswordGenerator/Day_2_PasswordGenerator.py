#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing necessary libraries

import random
import string

#defining function for password generation
#getting random characters genearated from uppercase, lowercase letters to
# digits and special characters
def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

#getting password length from user and storing it 

    passlen = int(input("Enter the password length")) 
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
#randomly shuffling the all the characters and printing

    random.shuffle(s)    
    pas = "".join(s[0:passlen])
    print(pas)
    
gen()

