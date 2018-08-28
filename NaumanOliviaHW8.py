#Olivia Nauman
#Introduction to Computer Science
#Practice set 8

#Sample 1
#This program takes, as an argument, a string called myString, and returns its reverse
def reverseString(myString):
    newString = ""
    for element in myString:
        newString = element + newString
    return newString

#Practice Problem 1
#This function takes, as an argument, a string and returns the string created by
#joining the string to its mirror. 
def mirrorString(aString):
    mirror=""
    for element in aString:
        mirror = element + mirror 
    return mirror + aString