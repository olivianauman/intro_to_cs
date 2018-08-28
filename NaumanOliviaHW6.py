#Olivia Nauman
#Intro to Computer Science
#Programming Practice 6

#Problem 1
#This function takes as an argument a positive integer n and returns the 
#sum of the first n perfect squares. 
def problem1(n):
    #create a counter to keep track of the number of times iterated
    counter = 1
    #create a value called perfectSum to keep track of the addition of squares
    perfectSum = 0
    #create a while loop to square n and each number before it
    while counter<(n+1):
        #add this value to perfect sum
        perfectSum = perfectSum + (counter**2)
        #add to the counter to avoid an endless loop
        counter = counter + 1
    return perfectSum

#Problem 2
#This function takes, as arguments, the slope of a line, the y-intercept
#of a line, and the x-coordinate of the point on the line. 
def problem2(slope,intercept,x):
    #use the form y=mx+b
    y=slope*x+intercept
    return y

#Problem 3
#This function takes, as an argument, a list, and returns a list that
#duplicates the elements in the list. 
def problem3(aList):
    #create an empty list
    newList=[]
    #create a loop to iterate through the values of that list
    for element in aList:
        #add each element to the new list twice
        newList.append(element)
        newList.append(element)
    return newList

#Problem 4
#This function takes, as an argument, two lists of distinct, positive
#integers, and returns the list whose sum is larger. 
def problem4(list1,list2):
    #create a variable to represent the sum of all values in the list.. set this equal to zero
    sumList1 = 0
    sumList2 = 0
    #create a loop to iterate through list1 and add each element to sumList1
    for element in list1:
        sumList1 = sumList1 + element
    #create a loop to iterate through list2 and add each element to sumList2    
    for element in list2:
        sumList2 = sumList2 + element
    #compare the values of sumList1 and sumList2
    if sumList1 > sumList2:
        return list1
    elif sumList1 < sumList2:
        return list2
    elif sumList1 == sumList2:
        return "They are equal."
    

        
        
