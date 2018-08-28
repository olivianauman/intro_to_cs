#Olivia Nauman
#Practice Set 9

#Practice Problem 1:
#This function takes, as an argument, a list of positive integers and a target value,
#and returns the number of times that the target value appears in the list. 
def problem1(myList,target):
    #make a counter to keep track of the number of times value appears
    counter=0
    #iterate through myList, adding one to the counter each time value appears
    for element in myList:
        if element == target:
            counter += 1
    return counter

#Practice Problem 2:
#This function takes, as an argument, a positive integer and returns the sum of its digits.
def problem2(value):
    #keep a total of the integers added, beginning with none; 0. 
    total=0
    #iterate through the value (type string)
    for digit in str(value):
        #for each digit, add the digit to the current total
        total = total + int(digit)
    return total

#Practice Problem 3:
#This function takes, as arguments, two strings: myString and charString, and counts the number
#of times that each letter in charString appears in myString and prints the answer as an
#output.
def problem3(myString,charString):
    total=0
    for element in charString:
        for character in myString:
            if character == element:
                
                total = total + 1
        print str(element) +"=" + str(total)
        total=0
