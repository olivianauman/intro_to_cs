#Battleship project
#2D arrays
def func():
    grid = []
    aList = [1,2,3,4]
    for i in range(0,4):
        grid.append(aList)
    for i in grid:
        print(i)
    for i in range(0,4):
        for j in range(0,4):
            print(grid[i][j])
            
#random function
import random
def randomFunc():
    #choose elements from a list using random.choice()
    aList = ['1','2','3','4']
    print(random.choice(aList))
    bList=[1.0,2.0,3.0,4.0]
    print(random.choice(bList))
    return 

#use a boolean variable to exit a while loop
#input integers from the user until the user enters an input > 10
def boolExit():
    inWhile = True
    while(inWhile == True):
        i = int(raw_input("Enter a number less than or equal to 10 to stay in the loop:"))
        if(i>10):
            inWhile=False
        return
    
#Calling helper functions
def matrixOps():
    #initialize the operand lists
    list1=[]
    list2=[]
    
    #create the operand lists
    for i in range(0,4):
        list1.append([1,2,3,4])
    for i in range(0,4):
        list2.append([4,3,2,1])
        
        #print the operand lists
        print("List 1")
        print(list1)
        print("List 2")
        print(list2)
        
        #call the helper function to add the operand lists (this helper function will be defined later)
        sumList = addLists(list1,list2)
        
        #print 
        print("Sum")
        print(sumList)
        return
    
def addLists(list1,list2):
    #initialize the list which will be returned
    returnList = []
    for i range(0,4):
        returnList.append([0,0,0,0])
        
    #perform the addition
    for i in range(0,4):
        for j in range(0,4):
            returnList[i][j] = list1[i][j] + list2[i][j]
    #return sum
    return returnList


#Quiz project
#counting input lines
#read test.txt and print each line with a line number
def lineCount():
    f=open("text.txt","r")
    lineNum=1
    for i in f:
        print("Line" + str(lineNum))
        print(i)
        lineNum += 1
    return
#read test.txt and print every 5th line
def fifthLine():
    f=open("test.txt","r")
    lineNum = 1
    for i in f:
        if (lineNum%5 ==0 0):
            print(i)
        lineNum+=1
    return

#read test.txt and sore every 5th line in a list. Return this list.
def listOfLines():
    f=open("test.txt","r")
    lineList = []
    lineNum = 1
    for i in f:
        if (lineNum%5 == 0):
            lineList.append(i.strip())
        lineNum += 1
    return lineList


def mainFunc():
    a = 1
    b = 2
    return multiply(a,b)

def multiply(a,b):
    return (a*b)
    
        
        