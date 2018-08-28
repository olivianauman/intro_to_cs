#Olivia Nauman
#Practice Program 7

#Sample One
import random
def createFile(n):
    fileName="myFile.txt"
    outputFile=open(fileName,"w")
    numbersToGenerate=n
    while numbersToGenerate>0:
        randomNumber=int(random.random()*1000)
        outputFile.write(str(randomNumber)+"/n")
        numbersToGenerate=numbersToGenerate-1
    outputFile.close()
#Sample Two    
def openFile():
    filename=raw_input("Enter a file name:")
    file=open(filename)
    target=raw_input("Enter a threshold value:")+"\n"
    counter=0
    for element in file:
        if (element==target):
            counter=counter+1
    print(str(counter)+" matches were found for target value "+str(target))
    file.close()
#Problem One
def createFile(myFile,n):
    outputFile=open(myFile)
    numbersToGenerate=n
    if n<1:
        return ("Enter a positive integer.")
    elif n<=1:
        while numbersToGenerate>0:
            randomNumber=int(random.randint(-1000,1001))
            outputFile.write(str(randomNumber)+"/n")
            numbersToGenerate=numbersToGenerate-1
        outputFile.close()  

#Problem Two
def maxValueInFile(fileName):
    file=open(fileName)
    Max=0
    for element in file:
        if element>Max:
            element=Max
    print Max       
            
#Problem Three
def minValueInFile(fileName):
    file=open(fileName)
    Min=""
    for element in file:
        if element<Min:
            element=Min
    print int(Min)
    
#Problem Four
def rangeOfValuesInFile(fileName):
    file=open(fileName)
    Min=""
    Max=0
    for element in file:
        if element>Max:
            element=Max    
    for element in file:
        if element<Min:
            element=Min
    print int(Max)-int(Min)
    
#Problem Five
def averageValueOnFile(fileName,n):
    file=open(fileName)
    Total=0
    amountOfValues=0
    for element in file:
        Total=Total+element
        amountOfValues=amountOfValues+1
    return Total / amountOfValues

#Problem Six
def greaterThanN(fileName,n):
    file=open(fileName)
    counter=0
    if n<-900 or n>900:
        return ("Your integer is out of range.")
    else:
        for element in file:
            if element>n:
                counter=counter+1
        return counter
    
#Problem Seven
def lessThanN(fileName,n):
    file=open(fileName)
    counter=0
    if n<-900 or n>900:
        return ("Your integer is out of range.")
    else:
        for element in file:
            if element<n:
                counter=counter+1
        return counter  
    
#Problem Eight
def createFile2(fileName):
    n=raw_input("Enter a positive integer")
    outputFile=open(fileName)
    numbersToGenerate=n
    if n<1:
        return ("Enter a positive integer.")
    elif n<=1:
        while numbersToGenerate>0:
            randomNumber=int(random.randint(-1000,1001))
            outputFile.write(str(randomNumber)+"/n")
            numbersToGenerate=numbersToGenerate-1
        outputFile.close() 
        
#Problem Nine
def greaterThanUser(fileName):
    n=raw_input("Enter an integer between -900 and 900.")
    file=open(fileName)
    counter=0
    if n<-900 or n>900:
        return ("Your integer is out of range.")
    else:
        for element in file:
            if element>n:
                counter=counter+1
        return counter     
#Problem Ten
def lessThanUser(fileName):
    n=raw_input("Enter an integer between -900 and 900.")
    file=open(fileName)
    counter=0
    if n<-900 or n>900:
        return ("Your integer is out of range.")
    else:
        for element in file:
            if element<n:
                counter=counter+1
        return counter    