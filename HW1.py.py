#Olivia Nauman

#Introduction to computer Science
#January 20, 2015
#Python Practice Assignment #1

#problem 1: this function takes two numbers, a and b, and subtracts one from the other respectively
#these two numbers, a and b, are taken as arguments
#this function, named subtractThem, returns the difference between a and b
def subtractThem(a,b):
    return a-b

#problem 2: this function is able to add three integers, taken as arguments, together.
#the name of the function is addEm.
#three variables are used in this function: a,b, and c
#each variable simply stands for one of three integers you wish to add together.
def addEm(a,b,c):
    return a+b+c

#problem 3: this function is able to take any given word and copy it any number of times consecutively
#these numbers are taken as arguments
#this function is named echo
#replace the word variable with the word you are seeking to duplicate
#replace the x variable with the number of times you would like the word duplicated
def echo(word,x):
    return (word)*x
				    
#problem 4: this function takes, as arguments, two strings and 
#returns a longer string 
#consisting of word1 copied 5 times and word2 copied 3 times 
def addwords(word1,word2):
    return ((word1)*5)+((word2)*3)

#problem 5: this function takes, as arguments, two values and 
#and returns a string describing the sum of their addition
#this function is called sumDescription
def sumDescription(value1,value2):
    return "the sum of "+str(value1)+" and "+str(value2)+" is "+str(value1+value2)

#problem 6: this function takes, as arguments, a name and a town, as strings
#and returns the two in a sentence reading
#Hello. My name is (name). I love the weather in (town).
#the name of this function is called introduction
def introduction(name,town):
    return "Hello. My name is "+str(name)+". I love the weather in "+str(town)+"."




