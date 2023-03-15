#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
print("This is a dice stimulator")
x = "y"

while x == "y":
    number = random.randint(1,6)

    if number == 1:
        print("----------")
        print("|        |")
        print("|    1   |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| 2    2 |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    3   |")
        print("|    3   |")
        print("|    3   |")
        print("----------")
    if number == 4:
        print("----------")
        print("| 4    4 |")
        print("|        |")
        print("| 4    4 |")
        print("----------")
    if number == 5:
        print("----------")
        print("| 5    5 |")
        print("|    5   |")
        print("| 5    5 |")
        print("----------")
    if number == 6:
        print("----------")
        print("| 6    6 |")
        print("| 6    6 |")
        print("| 6    6 |")
        print("----------")
    x = input("Press y to roll again")
    


# In[ ]:




