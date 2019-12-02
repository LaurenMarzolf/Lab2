def createMenu(listOfChoices, menuTitle):
    finalStr=menuTitle+"\n"
    ct=1
    for item in listOfChoices:
        finalStr+=str(ct)+". "+item+"\n"
        ct+=1
    return finalStr
