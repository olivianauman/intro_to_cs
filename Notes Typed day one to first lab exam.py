#Olivia Nauman
#FIRST LAB EXAM PRACTICE 

#This function returns the cost of shirts. The screenprinting cost is $50.
#This function calculates the cost of screenprinting and X shirts if each shirt
#costs $5 before screenprinting fees.
def shirtCost(x):
    return (x*5+50)/x

#This function takes, as an argument, a temperature in Celcius and converts
#it to Farenheit.
def cToF(temp):
    return 9/5 * int(temp) + 32


#This function, similarly, takes a list of temperatures in Celcius and converts
#them to Farenheit in a new list, using cToF as a helper function.
def CtoFList(aList):
    NewList=[]
    for element in aList:
        NewList.append(cToF(element))
    return NewList

#This function returns the max value of a list given as an argument
def findMax(aList):
    myMax = aList[0]
    for element in aList:
        if element > myMax:
            myMax = element
    return myMax

#This function returns the min value of a list given as an argument
def findMin(aList):
    myMin = aList[0]
    for element in aList:
        if element < myMin:
            myMin = element
    return myMin

#This function returns the relationship between one value squared and another
#value, taken as arguements.
def SquareLarger(x,y):
    if x**2 > y:
        return ("x squared is greater than y")
    elif x**2 < y:
        return ("x squared is less than y")
    elif x**2 == y:
        return ("x squared is equal to y")
    
#This function finds the MaxValue of aList using a While loop
def findMaxWhile(aList):
    maxValue = aList[0]
    counter = 0
    while (counter < len(aList)):
        if aList[counter] > maxValue:
            maxValue = aList[counter]
        counter = counter + 1
    return maxValue

#This function takes, as an argument, a positive integer n and returns a list of
#n random numbers between 0 and 1000. 
import random
def randomList(n):
    counter = 0 
    myList = []
    while (counter < n):
        randomNumber = random.randint(0,1001)
        myList.append(randomNumber)
        counter = counter + 1
    return myList
    
#This function takes, as an argument, a natural number n and returns the string 
#"prime" if it is prime and "composite" if it is composite. 
def isItaFactor(m,n):
    if n%m == 0:
        return True
    else:
        return False
def amIprime(n):
    for i in range (2,n-1):
        if (isItaFactor (i,n)==True):
            return "composite"
    else:
        return "prime"
        
#This function, tripler, takes a list as an argument, triples the values and 
#returns a list with those values tripled.
def tripler(aList):
    newList=[]
    for element in aList:
        triple=3*element
        newList.append(triple)
    return newList

#This function takes as an argument a slope and an intercept and returns
#the y coordinate.
def yCoord(slope,intercept):
    x = raw_input("What is the x coordinate on this line?")
    y = slope * float(x) + intercept
    return y

#This is the same as the last function, except all values are entered as raw_input
def yCoordRaw():
    x = raw_input("What is the x coordinate on this line?")
    m = raw_input("What is the slope coordinate on this line?")
    b = raw_input("What is the y-intercept of this line?")
    y=mx+b
    return y
    


