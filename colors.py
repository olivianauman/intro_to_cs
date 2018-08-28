def addColors():
    newList=[]
    c=""
    while (c != "quit"):
        c=raw_input("Enter a color,\"quit\" to exit:")
        if (c != "quit"):
            cInList= False
            for i in newList:
                if (i == c):
                    cInList= True
            if (cInList== False):
                newList.append(c)
    return newList
    
    
        