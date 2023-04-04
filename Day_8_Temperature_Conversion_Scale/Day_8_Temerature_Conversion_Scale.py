#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Welcome to Temperature Converter Scale")
print("-----------------------------------------")
print("Select one among the 6 choices given below")
print("-----------------------------------------------")
print("\n1.Temprature Conversion -- Celcius to Fahrenheit")
print("------------------------------------------------------")
print("\n2.Temprature Conversion -- Fahrenheit to Celcius")
print("------------------------------------------------------")
print("\n3.Temprature Conversion -- Kelvin to Celcius")
print("------------------------------------------------------")
print("\n4.Temprature Conversion -- Fahrenheit to Kelvin")
print("------------------------------------------------------")
print("\n5.Temprature Conversion -- Celcius to Kelvin")
print("------------------------------------------------------")
print("\n6.Temprature Conversion -- Kelvin to Fahrenheit")
print("------------------------------------------------------")

while True:
    # take input from the user
    choice = input("\nEnter choice(1/2/3/4/5/6): ")
    print("----------------------------------------")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = float(input("\nEnter temperature to be converted: "))
            print("------------------------------------------------------")
        except ValueError:
            print("\nInvalid input. Please enter valid temperature")
            continue
#to check among all the 6 possible conditions using the if-elif condition            
        if choice == '1':
            ctf = num1 * 1.8 + 32
            print('\n%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(num1, ctf))

        elif choice == '2':
            ftc = (num1 - 32) * 5/9
            print('\n%0.1f degree Fahrenheit is equal to %0.1f degree Celsius' %(num1, ftc))

        elif choice == '3':
            ktc = num1 - 273.15
            print('\n%0.1f degree Kelvin is equal to %0.1f degree Celsius' %(num1, ktc))

        elif choice == '4':
            ftk = 5 / 9 * (num1 - 32) + 273.15
            print('\n%0.1f degree Fahrenheit is equal to %0.1f degree Kelvin' %(num1, ftk))
        
        elif choice == '5':
            ctk = num1 + 273.15
            print('\n%0.1f degree Celsius is equal to %0.1f degree Kelvin' %(num1, ctk))
        
        elif choice == '6':
            ktf = 9 / 5 * (num1 - 273.15) + 32
            print('\n%0.1f degree Kelvin is equal to %0.1f degree Fahrenheit' %(num1, ktf))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        print("--------------------------------------------------------------")
        next_calculation = input("Let's do next calculation? (Yes/No): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")


# In[ ]:





# In[ ]:




