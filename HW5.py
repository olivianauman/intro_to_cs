#Olivia Nauman
#Intro to Comp Science
#Practice Set 5


#Practice Problem 1:
import random
#write a function that returns a list of 6 integers between 1 and 6.
def startTheGame():
    newList=[]
    counter=0
    while counter <6:
        newList.append(random.randint(1,6))
        counter=counter+1
    return newList

#Practice Problem 2:
#This function takes, as an argument, a list named aList. It returns a Boolean
#value 'True' if the elements in the list contains at least one integer and no more
#than six integers whose values range between 1 and 6. It returns the Boolean value
#'False' if the list conatins any other elements or is the wrong length.
def checkList(aList):
    correctList=True
    for element in aList:
        if len(aList)<1 or len(aList)>6:
            correctList=False        
        elif element <0 or element >6 :
            correctList=False
        elif type(element)!= int:
            correctList=False
    return correctList
        
           
            

#Practice Problem 3:
#This function takes as an argument a list named aList and an integer n. It then 
#returns aList with all values of n removed.
def removeValues(aList,n):
    newList=[]
    for element in aList:
        if element != n:
            newList.append(element)
            aList= newList
    return aList

#Practice Problem 4:
#This function takes, as an argument, a list named aList. It returns the number
#of 5s in the list multiplied by 50.
def fivePoints(aList):
    counter=0
    for element in aList:
        if element == 5:
            counter = counter + 1
    return counter * 50

#Practice Problem 5:
#This function takes, as an argument, a list named aList. It returns the number
#of 1s in the list multiplied by 100.
def onesPoints(aList):
    counter=0
    for element in aList:
        if element == 1:
            counter = counter + 1
    return counter * 100

#Practice Problem 6:
#Write a function that takes, as an argument, a list named aList and an integer n.
#It returns a Boolean True if the list contain exactly three elements equal to n,
#and returns a Boolean False otherwise.
def threeOfAKind(aList, n):
    counter=0
    for element in aList:
        if element == n:
            counter = counter+1
            if counter == 3:
                Three= True
            else:
                Three = False    
    return Three

#Practice Problem 7:
#Write a function that takes, as an argument, a list names aList, and two integers, 
# n and k. It returns a Boolean True if the list contains exactly k elements that 
#are equal to n and returns a Boolean False otherwise. 
def matchingValues(aList,n,k):
    counter=0
    IsIt=False
    for element in aList:
        if element == n:
            counter = counter+1
            if counter == k:
                IsIt= True
            else:
                IsIt = False    
    return IsIt    
              
#Practice Problem 8
#This function takes, as an argument, aList and returns a Boolean True
#if the list contains each of the integers between 1 and 6 exactly once, and
#false otherwise.
def isItAStraight(aList):
    Straight= False
    One=0
    Two=0
    Three=0
    Four=0
    Five=0
    Six=0
    for element in aList:
        if element == 1:
            One = One +1
        if element == 2:
            Two = Two +1
        if element == 3:
            Three = Three+1
        if element == 4:
            Four = Four +1
        if element == 5:
            Five = Five +1
        if element == 6:
            Six = Six +1
            
            if One==1 and Two==1 and Three==1 and Four==1 and Five==1 and Six==1:
                Straight= True
            else:
                Straight= False
    return Straight

#Practice Problem 9:
#This function takes, as an argument, a list called aList. 
#It returns a Boolean True if
#the list contains three pairs of integers and a false otherwise.
def threePairs(aList):
    uList= set(aList)
    x=len(uList)
    AreThere=False
    if x<=3:
        AreThere=True
    return AreThere

    
#Practice Problem 10:
#This function returns a list based on the other helper functions.
def playGame():
    theList = startTheGame()
    checkList(theList)
    print "The value of the fives is " +str(fivePoints(theList))+"."
    print "The value of the ones is " +str(onesPoints(theList))+"."
    for n in range(1,7):
        for k in range(3,7):
            testOne=matchingValues(theList,n,k)
            if testOne==True:
                print "There are " +str(k)+" "+str(n)+"s."
           # print "n is " + str(n) + " k is " + str(k)
    if isItAStraight(theList)==True:
        return "It is a straight!"
    if threePairs(theList)==True:
        return "There are three pairs."
    
    
    
        
    
    
    
    





            
        
        
            