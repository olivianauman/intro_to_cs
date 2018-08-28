#This is a function that asks for a list of 6 values and returns 
#a new list with their squares.
def squareMyList():
    myList= raw_input("Please enter a list of six integers.")
    newList=[]
    for element in myList:
        square= element**2
        newList.append(square)
    return newList

#This function takes, as an argument, a value in L and returns it in milliliters
def mLtoL(L):
    return str(L*1000) + " milliliters"
        
    
