# ACRONYM DEFINER
# AUTHOR: Cole Horvat

# DESCRIPTION: Gives the user two options, to input a definition for an acronym or to process a statement.

# The first option will ask for an acronym then a definition to that acronym. These are stored in a dictionary,
# which is then stored in a file so the acronym and definition can be accessed even if you terminate the program.

# The second option lets you input a statement. If you defined an acronym, and put the acronym in your statement,
# the statement will change the have the definition of the acronym in your statement.

def addAcronyms(readFile, acroDict):
    for i in readFile:
        initialString = i
        acroString = initialString.split(":")[0]
        defString = initialString.split(":")[1]
        defString = defString.replace("\n", "")
        acroDict[acroString] = defString


def evalStatement(userStatement, acroDict):
    wordList = userStatement.split(" ")
    finalStatement = ""

    for j in wordList:
        if j in acroDict:
            newString = j + " (" + acroDict[j] + ") "
            finalStatement += newString
        else:
            finalStatement += j + " "

    print(finalStatement)

writeFile = open("inputdata.txt", "w")
readFile = open("inputdata.txt", "r")
acroDict = {}

try:
    addAcronyms(readFile, acroDict)
except IndexError:
    print("")

readFile.close()
while True:
    appendFile = open("inputdata.txt", "a")
    print("*********************************************")
    print("               ACRONYM DEFINER               ")
    print("*********************************************")
    print("\nWhat would you like to do?")
    print("1. Define an acronym")
    print("2. Process a statement")
    userInput = input()

    if userInput == "1":
        acronym = input("Please enter the acronym that you want to define >> ")
        acronym = acronym.upper()

        if acronym in acroDict:
            print(acronym + " is already defined")
            continue

        acroDict[acronym] = input("What is the definition of " + acronym + "? >> ")
        acroDict[acronym] = acroDict[acronym].lower()
        appendFile.write(acronym + ":" + acroDict[acronym])
        appendFile.write("\n")
        appendFile.close()
        print(acronym + " is defined!")

    if userInput == "2":
        userStatement = input("Enter a statement or paragraph you want to process >> ")
        evalStatement(userStatement, acroDict)

writeFile.close()