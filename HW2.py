#Olivia Nauman
#Intro to Computer Science
#20 January 2016
#Python Practice Assignment #2

#Sample 1:
#This function takes, as an argument, an integer n, and returns a list of n 
#random integers with values between 0 and 9.
import random
def randomNumbers(n):
    
    #create an empty list
    myList = []
    
    #introduce a Boolean, called needMoreNumbers, to keep track of whether or 
    #not we need more numbers
    needMoreNumbers = True
    
    #we will iterate through the process, creating new numbers if we need them.
    #A boolean is either True or False. If the boolean needMoreNumbers is False,
    #we will exit this loop. but until we reset the boolean needMoreNumbers
    #to be False, we will continue to iterate through this loop
    
    while(needMoreNumbers):
        #create a random integer between 0 and 9, inclusive
        randomNumber = int(random.random() * 10)
        
        #add the random number to the list of random numbers using the append()
        #method
        myList.append(randomNumber)
        
        #decrease the number to create by 1, to make progress towards getting 
        #out of the loop
        n=n-1
        
        #decide whether or not to keep going:
        if (n < 1):
            needMoreNumbers = False
            
    return myList

#Practice Problem 1:
#write a function called randNum(n), which takes, as an argument, an integer n, 
#and returns a list of n random integers with values between 0 and 9. To do this,
#use a for loop. 
def randNum(n):
    #create an empty list
    myList = []  
    #create a for loop which iterates values from 0 to n-1 times
    for looptimes in range(0,n):
        #define randomNumber #allow random numbers up to 10
        randomNumber = int(random.random() * 10)
        #add random numbers to myList until you reach n values on list
        myList.append(randomNumber)
    #return myList
    return myList

#Practice Problem 2:
#write a function called randNumMaxFor(n,maxValue), which takes, 
#as an argument, an integer n and an integer maxValue, and returns 
#a list of n integers > maxValue
def randNumMaxFor(n,maxValue):
    #create an empty list
    myList=[]
    #create a for loop which interates values from 0 to n-1 times
    for looptimes in range(0,n):
        #define randomNumber #allow random numbers up to maxValue
        randomNumber=int(random.random()*maxValue)
        #add random number to list until n values are achieved
        myList.append(randomNumber)
    #return myList    
    return myList

#Practice Problem 3:
#write a function, called randNumMaxWhile(n,maxValue), that generates a list
#of n random numbers between 0 and maxValue. It will use a while loop to do this
def randNumMaxWhile(n,maxValue):
    #create an empty list
    myList=[]
    needMoreNumbers=True
    while (needMoreNumbers):
        randomNumber=int(random.randrange(0,maxValue))
        myList.append(randomNumber)
        n=n-1
        if (n<1):
            needMoreNumbers=False
    return myList

#Practice Problem 4:
#write a function, called randNumMinFor(n,minValue), which generates a list of n
#values between minValue and 1000. This function should use a for loop to 
#generate the list
def randNumMinFor(n,minValue):
    #create an empty list
    myList=[]
    #create a loop which iterates values from 0 to n-1 times
    for looptimes in range(0,n):
        #define randomNumber #allow numbers above minValue
        randomNumber=int(random.randrange(minValue,1000,1))
        #add random number to list until n values are achieved
        myList.append(randomNumber)
    #return myList
    return myList

#Practice Problem 5:
#write a function, called randNumMinWhile(n,minValue), that generates a list
#of n random numbers between 0 and minValue. It will use a while loop to do this
def randNumMinWhile(n,minValue):
    #create an empty list
    myList=[]
    #create boolean condition
    needMoreNumbers=True
    while(needMoreNumbers):
        #generate random number between minValue and 1000
      randomNumber=int(random.randrange(minValue,1000)) 
      #add that value to the list
      myList.append(randomNumber)
      n=n-1
      #add numbers until you reach n numbers
      if (n<1):
          needMoreNumbers=False
    #return myList
    return myList

#Practice Problem 6:
#write a function, called randNumMinMaxFor(n,minValue,maxValue), that 
#generates a list of n random numbers between minValue and maxValue. This
#function should use a for loop.
def randNumMinMaxFor(n,minValue,maxValue):
    #create an empty list
    myList=[]
    #create a loop which iterates values from 0 to n-1 times
    for looptimes in range(0,n): 
        #define randomNumber #allow numbers above minValue
        randomNumber=int(random.randrange(minValue,maxValue,1))   
        #add random number to list until n values are achieved
        myList.append(randomNumber)
    #return myList
    return myList

#Practice Problem 7:
#write a function, called randNumMinMaxWhile(n,minValue,maxValue), that 
#generates a list of n random numbers between minValue and maxValue. This
#function should use a while loop.
def randNumMinMaxWhile(n,minValue,maxValue):
    #create an empty list
    myList=[]
    needMoreNumbers=True
    while (needMoreNumbers):
        randomNumber=int(random.randrange(minValue,maxValue))
        myList.append(randomNumber)
        n=n-1
        if (n<1):
            needMoreNumbers=False
            return myList
        
#Sample 2:
#This takes, as arguments, two values: a list and a target value.
#It returns the number of times that the target value appears in the list.
def countTarget(myList,target):
    #initialize the counter to zero
    counter=0
    for element in myList:
        #compare the value in the list to the target value...if they are the
        #same, increment the counter
        if element==target:
            counter=counter+1
    return counter

#Practice Problem 8:
#This takes, as arguments, two values: a list and a target value.
#It returns the number of values in the list that are greater than the 
#target value. This function is called countAboveTarget(myList,target).
def countAboveTarget(myList,target):
    #initialize the counter to zero
    counter=0
    for element in myList:
        #compare the value in the list to the target value...if the list is
        #larger than the target increment the value
        if element>target:
            counter=counter+1
    return counter

#Practice Problem 9:
#This takes, as arguments, two values: a list and a target value.
#It returns the number of values in the list that are less than the 
#target value. This function is called countBelowTarget(myList,target).
def countBelowTarget(myList,target):
    #initialize the counter to zero
    counter=0
    for element in myList:
        #compare the value in the list to the target value...if the list is
        #smaller than the target increment the value
        if element<target:
            counter=counter+1
    return counter       
            
#Practice Problem 10:
#This function, called usingFunctionsGreater(n), takes, as an argument, 
#a positive integer n. It generates three random numbers between 200 and 625.
#call the smallest number minValue, the middle value should be called myTarget
#and the largest should be called maxValue. Then, call Prac.Prob. 6 function
#to generate listof n random numbers between minValue and maxValue. Call list
#myList. Pass myList and myTarget into Prac.Prob. 8.

def usingFunctionsGreater(n):
    #generate a list of three random numbers between 200 and 625
    MyList = randNumMinMaxFor (3,200,625)
    #sort MyList from smallest to largest. Define minValue, maxValue, and a 
    #target value called myTarget
    MyListSorted = sorted (MyList)
    minValue = MyListSorted[0]
    myTarget = MyListSorted[1]
    maxValue = MyListSorted[2]
    #count the number of values on MyList that are greater than myTarget
    CountValues = countAboveTarget(MyList,myTarget)
    return CountValues

#Practice Problem 11:
#Write a function called usingFunctionsLess(n) that takes, as an argument, 
#a positive integer n. It generates three random numbers between 200 and 625.
#call the smallest number minValue, the middle value should be called myTarget
#and the largest should be called maxValue. Then, call Prac.Prob. 6 function
#to generate list of n random numbers between minValue and maxValue. Call list
#myList. Pass myList and myTarget into Prac.Prob. 9 to find the number of 
#elements in the list that are less than myTarget. Return this value.
def usingFunctionsLess(n):
    #generate a list of three random numbers between 200 and 625
    MyList = randNumMinMaxFor (3,200,625)
    #sort MyList from smallest to largest. Define minValue, maxValue, and a 
    #target value called myTarget
    MyListSorted = sorted (MyList)
    minValue = MyListSorted[0]
    myTarget = MyListSorted[1]
    maxValue = MyListSorted[2]
    #count the number of values on MyList that are less than myTarget
    CountValues = countBelowTarget(MyList,myTarget)
    return CountValues

#Practice Problem 12:
#Write a function called calculateAverage(n) that takes the function in Practice
#Problem 1 and utilizes it to generate a list of n random numbers between 0 and 9.
#Next, calculate the average of these numbers.
def calculateAverage(n):
    #generate a list of n random numbers. Name this list myList
    myList= randomNumbers(n)
    #calculate the average of the values in myList by taking the sum of the
    #integers divided by the number of integers. Call the result myAverage
    myAverage=sum(myList)/len(myList)
    #return myAverage
    return myAverage
    

    
    






         
    
    