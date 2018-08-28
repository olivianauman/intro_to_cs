#This is how to create a new text file
def newFile():
    file = open("examplefile.txt","w")
    file.write("You could write line one like this." +"\n")
    file.write("and a second line could look like this!")
    file.close()
    return "All is well!"
    


#This algorithm will create a file and write integers 1-1000 in seperate lines to it
def writefile():
    #note that the file name is numbers.text and that you are WRITING ('w') to this file, as opposed to the default reading setting.
    f = open("numbers.txt",'w')
    numbers = ""
    #note that the second integer in the range function is not inclusive
    for i in range(1,1001):
        #note that \n is the NEXT LINE command
        numbers = numbers + str(i) +"\n"
    #write the string "numbers" to numbers.text
    f.write(numbers)
    #DON'T YOU DARE forget to close the file!
    f.close()
    return "Compilation successful!"

#This algorithm will read numbers from the file and print the even numbers
def evenlines():
    f = open("numbers.txt")
    for line in f:
        if(int(line)%2 == 0):
            print (line)
    f.close()
    return

#This algorithm counts the number of works that begin with A (not case sensitive) 
#in the text file and returns the total count
def countwords():
    f = open("test.txt")
    count=0
    for line in f:
        myList=line.split()
        for word in myList:
            if (word.startswith("a")) or (word.startswith("A")):
                counter = counter + 1
    f.close()            
    return count

#This function determines the cost of shirts if there is a screenprinting cost of $50 and shirts cost $8
def shirtCost(NumberofShirts):
    Totalcost = 50 + (8 * NumberofShirts)
    return Totalcost/NumberofShirts

#This function takes a string as an argument and returns the string and its mirror
def mirrorString(string):
    mirror=""
    for letter in string:
        mirror = letter + mirror
    return string + mirror
        
#The following function takes, as an argument, a list of numbers, and returns the word EVEN if the length is even along with the sum of the lists values and ODD along with a sum of the values if odd
def OddOrEven(aList):
    HowMany= len(aList)
    if HowMany % 2 == 0:
        return "EVEN" + str(sum(aList))
    if HowMany % 2 == 1:
        return "ODD " + str(sum(aList))
    
#The following function will take my chem scores as raw input and give me my score back
def ChemScore():
    Exam1= raw_input("What was your Exam 1 score (out of 150)?")
    Exam2= raw_input("What was your Exam 2 score (out of 150)?")
    Exam3= raw_input("What was your Exam 3 score (out of 150)?")
    FinalExam= raw_input("What was your Final Exam score (out of 200)?")
    Labs= raw_input("How many points (out of 200) did you recieve on lab and case study projects?")
    MasteringChemistry= raw_input("How many points (out of 120) did you earn on Mastering Chem Assignments?")
    Discussion= raw_input("How many Discussion Sections points did you earn (out of 30)?")
    FinalScore= int(Exam1) + int(Exam2) + int(Exam3) + int(FinalExam) + int(Labs) + int(MasteringChemistry) + int(Discussion)
    if FinalScore==0 or FinalScore<591:
        return "Your grade is an F before the curve." + "You have a score of " + str(FinalScore)
    elif FinalScore>590 and FinalScore<661:
        return "Your grade is a D before the curve." + "You have a score of "+str(FinalScore)  
    elif FinalScore>660 and FinalScore<691:
        return "Your grade is a D+ before the curve." + "You have a score of " +str(FinalScore)  
    elif FinalScore>690 and FinalScore<721:
        return "Your grade is an C- before the curve." + "You have a score of " +str(FinalScore)   
    elif FinalScore>720 and FinalScore<761:
        return "Your grade is an C before the curve." + "You have a score of " +str(FinalScore)                
    elif FinalScore>760 and FinalScore<791:
        return "Your grade is an C+ before the curve." + "You have a score of " +str(FinalScore)     
    elif FinalScore>790 and FinalScore<831:
        return "Your grade is an B- before the curve." + "You have a score of " +str(FinalScore)  
    elif FinalScore>830 and FinalScore<871:
        return "Your grade is an B before the curve." + "You have a score of " +str(FinalScore) 
    elif FinalScore>870 and FinalScore<891:
        return "Your grade is an B+ before the curve." + "You have a score of " +str(FinalScore)      
    elif FinalScore>899 and FinalScore<939:
        return "Your grade is an A- before the curve." + "You have a score of " +str(FinalScore)
    elif FinalScore>939:
        return "Your grade is an A before the curve." + "You have a score of " + str(FinalScore)

        
#This program takes a number, n, and returns a sum of the first n perfect squares
def PerfectSum(n):
    counter = 1
    perfectSum = 0
    while counter < (n + 1):
        perfectSum += (counter **2)
        counter += 1
    return perfectSum

#This function takes, as an argument, a list, and returns a list that
#duplicates the elements in the list. 
def doubleList(aList):
    newList=[]
    for element in aList:
        newList.append(element)
        newList.append(element)
    return newList
        
#This function takes, as an argument, two lists of distinct, positive
#integers, and returns the list whose sum is larger. 
def problem4(list1,list2):
    if sum(list1) > sum(list2):
        return list1
    elif sum(list1) < sum(list2):
        return list2
    else:
        return "The two lists are equal."
    
#This function takes as an argument a list named aList and an integer n. It then 
#returns aList with all values of n removed.
def removeValues(aList,n):
    newList=[]
    for element in aList:
        if element != n:
            newList.append(element)
    return newList

#This function takes, as an argument, a list named aList. It returns the number
#of 5s in the list multiplied by 50.
def fivePoints(aList):
    counter=0
    for element in aList:
        if element == 5:
            counter += 1
    return counter * 50

import random
#this function generates a random number between 1 and 20 and asks the user to
#guess the number until the correct natural number is entered
def playGame3():
    #generate a random number
    number=random.randint(1,20)
    #ask user to guess the number
    guess=raw_input("I'm thinking of a number between 1 and 20. Guess what it is:")
    #while the guess is wrong, ask for another guess
    while (number != int(guess)):
        print ("Nope! Guess again!")
        guess=raw_input("I'm thinking of a number between 1 and 20. Guess what it is:")
    #when they guess correctly, tell them they have   
    else:
        return ("Excellent! You guessed the number!")
    
#this function takes, as an argument, a character and a string. It then returns
#a Boolean saying whether the character is found within the string. This function
#is case sensitive. Values entered as arguments should be entered as strings.
def isItThereS(letter,word):    
    IntheWord = False
    for element in word:
        if letter == element:
            IntheWord = True
    return IntheWord

def tripler(aList):
    tripleList=[]
    for element in aList:
        tripleList.append(element)
        
    return tripleList

    