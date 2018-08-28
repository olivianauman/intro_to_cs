#A function to find the exponent of inputs x and y
def expFor(x,y):
    result = 1
    for i in range(0,y):
        result = result * x
    return result

def expWhile(x,y):
    result = 1
    check = True
    while(check):
        result = result * x
        y = y - 1
        if(y == 00):
            check = False
    return result

#ANOTHER WAY OF DOING IT
def expWhile(x,y):
    result = 1
    while(y != 00):
        result = result * x
        y = y - 1
    return result

#Function that returns the sum of the elements if a list
def sumFor(aList):
    sum = 0
    for i in aList:
        sum = sum + i
    return sum

def sumWhile(aList):
    sum = 0
    i = 0
    n = len(aList)
    check = True
    while(check):
        sum = sum + aList[i]
        i = i + 1
        if(i == n):
            check = False
        return sum
    
    
#Another way of doing that
def sumWhile(aList):
    sum = 0
    i = 0
    n = len(aList)
    check = True
    while(i<n):
        sum = sum + aList[i]
        i = i + 1
    return sum

#Function to input a list and create a new list with every element doubled
def doubleFor(aList):
    #Create a new empty list
    newList = []
    #iterate through each element in aList
    for i in aList:
    #double the element and append it to newList
        newList.append(i * 2)
    #return newList
    return newList

def doubleWhile(aList):
    newList = []
    i = 0
    while(i < len(aList)):
        newList.append(aList[i] * 2)
        i = i + 1
    return newList

#Quiz Question
#What is myFun[1,-1,2,-6]?
def myFun(aList):
    sum = 0
    for element in aList:
        if(element > 0):
            sum = sum + element
    return sum
#ANSWER: 3
