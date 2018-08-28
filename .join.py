#Get the index where myChar occurs replace the calue in myWord at that index
#with the string "$$", i.e. reassign the value at that index as "$$".
def problem4(myWord,myChar):
    charList = list(myWord)
    if myChar not in myWord:
        return ("Character not found.")
    else:
        while myChar in charList:
            charList[charList.index(myChar)] = "$$"
        return "".join(charList)
    
def problem1(numberOfDollars):
    quarters = numberOfDollars * 4
    if (numberOfDollars == 0) or (numberOfDollars > 1):
        return "There are "+str(quarters)+" quarters in "+str(numbersOfDollars)+" dollars."
    elif numberOfDollars == 1:
        return "There are "+str(quarters)+" quarters in "+str(numbersOfDollars)+" dollar."
    
#"\n" new line character in a file

def tryThis(myString):
    newString = ""
    for char in myString:
        if char == 'A':
            newString = '4' + newString
        return newString