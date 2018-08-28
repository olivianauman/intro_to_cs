#Olivia Nauman
#Practice Four: Sample Lab Exam One
#Intro to Computer Science

#Problem 1:
#This function takes, as arguments, the length and width of a rectangle (in 
# inches) and returns the area of the rectangle. 
def problem1(length,width):
    #the area of a rectangle is the length times the width
    theArea = length * width
    #the result should be returned in the sentence "The area of the rectangle
    #is ____________(area of rectangle in blank) square inches."
    return "The area of the rectangle is " + str(theArea) + " square inches."

#Problem 2:
#This function takes, as an argument, a list of positive numbers. This list is
#called aList. If aList has an even number of elements the function returns the 
#sum of aList. If there is an odd number of elements, it returns a list the same length as aList with all elements being the length of aList
def problem2(aList):
    #theRemainder is what is leftover after dividing aList by 2
    theRemainder = len(aList)%2
    #if the number is even, theRemainder should equal 0
    if theRemainder == 0:
        #return the sum of all elements in aList
        return sum(aList)
    #if the number is odd, theRemainder should equal 1
    elif theRemainder == 1:
        #create an empty list
        newList=[]
        for element in aList:
            #each element in aList is positive... so they are all>0.
            if element>0:
                #you add the number of items in aList to newList the number
                #of times aList has elements
                newList.append(len(aList))
        #return the resulting list        
        return newList
        
#Problem 3:
#This function takes a list of numbers, as an argument, and returns a new list 
#of those values squared. 
def problem3(aList):
    #create the new list, empty to begin with
    squaredList=[]
    for element in aList:
        #square each element of aList and add it to squaredList
        squaredList.append(element*element)
    #return the user the squared list of integers    
    return squaredList

#Problem 4:
#This function takes, as arguments, two strings and returns a sandwich of the 
#two strings in the arrangement string one string two string one
def problem4(myString1,myString2):
    return myString1 + myString2 + myString1