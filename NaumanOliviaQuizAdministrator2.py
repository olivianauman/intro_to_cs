#Olivia Nauman
#Introduction to Computer Science Final Project
#This program was written on Python 2.7.11
#I referenced this list for certain functions in my program https://docs.python.org/2/library/functions.html


def administerQuiz(filename):
    #open the file for reading
    fileGiven = open(filename,'r')
    #make an empty list to keep track of the contents of the file
    fileLines = []
    #Add each line to the empty list
    for line in fileGiven:
        fileLines.append(line.replace('\t',' '))
    for element in fileLines:
        for word in element:
            word.rstrip()
    k = int(fileLines[0]) #this is the number of questions
    n = int(fileLines[1]) #this is the number of choices to the questions
    #This counter keeps track of the index of the question being worked with
    QuestionYouAreOn = 2
    #This counter keeps track of the index of the correct answer
    correctAnswer = 2 + n + 1
    #This counter keeps tack of the amount of correctly answered questions
    scoreCounter = 0
    #beginning and end will be the first and last indexes the question answers fall on
    beginning = QuestionYouAreOn + 1
    end = QuestionYouAreOn + n + 1
    #This counter will act as a way to number the questions
    choice = 1
    #This print statement introduces the quiz to the user
    print "The following quiz is multiple choice. Please answer each of the " + str(k) + " questions with the number in front of your answer. Good Luck!"
    #while you are not yet through all of the questions
    while len(fileLines) > QuestionYouAreOn:
        #print the question
        print fileLines[QuestionYouAreOn]
        #print the answers with the choice number in front of it
        #for each line in the range(first answer choice to last answer choice)
        for line in fileLines[beginning:end]:
            #This variable is the last answer choice
            keepTrack = QuestionYouAreOn + n
            #This variable is the question index
            PrintAnother = QuestionYouAreOn
            #As you approach the last answer choice, print each line
            if  PrintAnother < keepTrack:
                print (str(choice) + ". " + str(line))
            #increment counters
            PrintAnother = PrintAnother + 1
            choice = choice + 1
        choice = 1
        beginning = beginning + 2 + n
        end = end + n + 2
        #ask user to answer the question with a guess, and then compare this value to the correct answer
        answer = raw_input("What is the correct answer? (Reply with the numeral before your choice (1,2,3..etc.)")
        if answer == (fileLines[correctAnswer]):
            #let them know if they get the correct answer and add a point to their score
            print "Correct!"
            scoreCounter = scoreCounter + 1
        elif answer != (fileLines[correctAnswer]):
            #let them know if they don't get the correct answer and do nothing to their score
            print "Incorrect! The correct answer was " + str(fileLines[correctAnswer]) + "." 
            #Increment both the question counter and the correct answer counter to continue moving through the quiz
        QuestionYouAreOn = QuestionYouAreOn + n + 2
        correctAnswer = correctAnswer + n + 2
    #evaluate how well the user has done on the quiz
    HowWell = ""
    #divide the number they got correct by the potential number correct. This gives a decimal so multiply by 100.
    percentageScoreCounter = (float(scoreCounter)/float(k)) * 100
    if percentageScoreCounter >= 90:
        HowWell = "You aced the quiz! Fantastic!"
    elif percentageScoreCounter < 90 and percentageScoreCounter >= 75:
        HowWell = "Great Job!"
    elif percentageScoreCounter < 75 and percentageScoreCounter >= 60:
        HowWell = "C's get degrees!"
    elif percentageScoreCounter < 60 and percentageScoreCounter >= 45:
        HowWell = "You passed... barely." 
    elif percentageScoreCounter < 45:
        HowWell = "You failed the quiz! Better luck next time." 
    return "You answered " + str(scoreCounter) + " questions correctly out of "+ str(k) + " questions. " + HowWell
    fileGiven.close()
    





    
    
    
        
    
    
    

    