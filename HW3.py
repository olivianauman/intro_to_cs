#Olivia Nauman
#Intro to Computer Science
#01 February 2016
#Python Practice Assignment 

#Sample Problem 1:
#This program asks the user for input from the keyboard and returns what they 
#typed
def typeSomething():
    #ask the user for input.
    choice=raw_input("Type something:")
    
    #return what they typed
    print(type(choice))
    return choice

#Sample Problem 2:
import random
#this function generates a random number between 1 and 20 and asks the user to 
#guess the number
def playGame():
    number=random.randint(1,20)
    guess=raw_input("I'm thinking of a number between 1 and 20. Guess what it is:")
    #the input from a keyboard is a string... and the random number generated is
    #an int. If we want to compare them to each other, we need to compare the 
    #same data types!
    if number==int(guess):
        print("That is correct!")
    else:
        print("Nope...I was thinking of "+str(number)+".")

#Practice Problem 1:
import random
#this function generates a random number between 100 and 200 and asks the user
#to guess the number.
def playGame2():
    number=random.randint(100,200)
    guess=raw_input("I'm thinking of a number between 100 and 200. Guess what it is:")
    #the input from a keyboard is a string... and the random number generated is
    #an int. If we want to compare them to each other, we need to compare the 
    #same data types! (strings)
    if str(number)==(guess):
        print("That is correct!")
    else:
        print("Nope...I was thinking of "+str(number)+".")
        
#Practice Problem 2:
import random
#this function generates a random number between 1 and 20 and asks the user to
#guess the number until the correct natural number is entered
def playGame3():
    #generate a random number
    number=random.randint(1,20)
    #ask user to guess the number
    guess=raw_input("I'm thinking of a number between 1 and 20. Guess what it is:")
    #while the guess is wrong, ask for another guess
    while (number != int(guess)):
        print ("Nope! Guess again!")
        guess=raw_input("I'm thinking of a number between 1 and 20. Guess what it is:")
    #when they guess correctly, tell them they have   
    else:
        return ("Excellent! You guessed the number!")
        
    
#Practice Problem 3:
import random
#this function generates a random number between 1 and 20 and asks the user to
#guess the number until the correct natural number is entered. When the correct
#answer is given, the string "Excellent! You guessed the number in (number of 
#tries) tried!"
def playGame4():
    #generate a random number
    number=random.randint(1,20)
    #ask the user to guess what that number is
    guess=raw_input("I'm thinking of a number between 1 and 20. Guess what it is:")
    counter=1
    #while the guess is incorrecr, ask them to guess again and adjust counter accordingly
    while (number != int(guess)):
            print ("Nope! Guess again!")
            guess=raw_input("I'm thinking of a number between 1 and 20. Guess what it is:")
            counter = counter + 1
            
    #when they guess correctly, tell them the number of tries it took
    else:
            return ("Excellent! You guessed the number in " + str(counter)+ " tries!")    
    

#Practice Problem 4:
#this function takes, as an argument, a character and a string. It then returns
#a Boolean saying whether the character is found within the string. This function
#is case sensitive. Values entered as arguments should be entered as strings.
def isItThereS(letter,word):
    InTheWord = False
    #InTheWord will remain false until it encounters a letter within the word
    for character in word:
        if letter == character:
            InTheWord = True
    return InTheWord

#Practice Problem 5:
#this function takes, as an argument, a character and a string. It then returns
#a Boolean saying whether the character is found within the string. This function
#is NOT case sensitive. Values entered as arguments should be entered as strings.
def isItThereIn(letter,word):
    #InTheWord remains false until proven true
    InTheWord = False
    #if a letter is in the word, InTheWord becomes true (regardless of upper or lower case)
    for character in word.lower():
        if letter.lower() == character.lower():
            InTheWord = True
    return InTheWord

#Practice Problem 6:
#this function takes, as an argument, a character and a string. It returns
#the number of times that the character can be found in the string. This function
#IS case sensitive!
def howOftenS(letter,word):
    #InTheWord remains false until proven true
    InTheWord = False
    counter=0
    #if a letter is in the word, InTheWord becomes true (case sensitive)
    for character in word:
            if letter == character:
                InTheWord = True
                #each character that meets criteria adds one to the counter
                counter=counter + 1
    return counter   

#Practice Problem 7:
#this function takes, as an argument, a character and a string. It returns
#the number of times that the character can be found in the string. This function
#IS NOT case sensitive!
def howOftenIn(letter,word):
    #InTheWord remains false until proven true
    InTheWord = False
    counter=0
    #if a letter is in the word, InTheWord becomes true (case insensitive)
    for character in word.lower():
                if letter.lower() == character.lower():
                    InTheWord = True
                     #each character that meets criteria adds one to the counter
                    counter=counter + 1
                
    return counter   
    
#Practice Problem 8:
#this function takes, as an argument, a character and a string. It returns the
#first index that the character can be found in the string. If the letter is not 
#in the string, it should return "It is not there." This function IS case
#sensitive.
def whereIsItS(letter,word):
        #the counter is set at -1 because it is observing the position of the letter
        counter = -1
        #if a letter is in the word, InTheWord becomes true (case sensitive)
        for character in word:
            #each character that meets criteria adds one to the counter
            counter=counter + 1            
            if letter == character: 
                return counter
            else:
                counter == counter
                #If this is the case, return "It is not there."
        return "It is not there."
            

#Practice Problem 9:
#this function takes, as an argument, a character and a string. It returns the
#first index that the character can be found in the string. If the letter is not 
#in the string, it should return "It is not there." This function IS NOT case
#sensitive.
def whereIsItIn(letter,word):
    #the counter is set at -1 because it is observing the position of the letter
            counter = -1
            #if a letter is in the word, InTheWord becomes true (case sensitive)
            for character in word.lower():
                #each character that meets criteria adds one to the counter
                counter=counter + 1            
                if letter.lower() == character.lower(): 
                    return counter
                else:
                    counter == counter
                    #If this is the case, return "It is not there."
            return "It is not there."    
    
