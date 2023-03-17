#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import random
def hangman():

    #Fruit bank to guess any one among fruits below
    word = random.choice(["apple" , "banana" , "cherry" , "date" , "eggplant" , "fig" , "grapes" , "huckleberry" , "jackfruit" , "kiwi" , "lime" , "mango" , "noctraine" , "orange" , "pears" , "quine" , "raspberry" , "strawberry" , "tamarind" , "ugli" , "velvet-apple" , "watermelon"  ])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    #checking for the fruit word length
    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the right fruit:" , main)
        guess = input()
#validating the letters if they are correct and form the right fruit name out ogf the fruit bank
        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()
#the game starts here, the hangman is made after each inorrect iteration of letter entered by user   
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left, Try your best")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left, Predict the correct fruit please")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left, You are almost halfway to win or lose")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left, Recall your favorite fruit")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("Oops Hangman lost a life!")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name = input("Enter your name: ")
print("Welcome " , name )
print("-------------------")
print("Try to guess the accurate fruit in less than 10 attempts")
hangman()
print()


# In[ ]:




