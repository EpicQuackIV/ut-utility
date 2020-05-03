import glob

# Note: Don't use this on behavior files that won't compile

#######################################################
#                                                     #
#  The Cooldown Machine, for fixing broken cooldowns  #
#                                                     #
#######################################################

def cools(path, toReplace = "coolDown:", minCool = 200, roundTo = 0, formatAdd = " "):
    '''
    path: specifies which files to replace cooldowns in
    toReplace: keyword before cooldowns. i.e. use "coolDownOffset:" if fixing coolDownOffset cooldowns
    minCool: cooldowns that are lower than minCool are set to minCool
    roundTo: all cooldowns are rounded up to the nearest roundTo. if roundTo is 0 then no cooldowns will be rounded.
    formatAdd: used to add a space between toReplace and the new cooldown
    '''
    for fileName in glob.glob(path):
        updates = []
        fo = open(fileName, "r")
        fileArr = fo.read().split(toReplace)
        fo.close()

        for x in range(1, len(fileArr)):
            cool = fileArr[x]
            newCool = getNewCool(cool, minCool, roundTo, toReplace + formatAdd)
            fileArr[x] = newCool[0]
            if (newCool[1]):
                updates.append(x)

        fileDispName = fileName[fileName.rfind("/") + 1:]
        newFileText = "".join(fileArr)
        printFileUpdates(fileDispName, updates, toReplace)
        replaceFileText(fileName, newFileText)

def getNewCool(oldCoolText, minCool, roundTo, prefix):
    '''
    Sets numbers lower than minCool to minCool
    Sets everything to multiples of roundTo. Useful for getting rid of weird numbers
    '''
    info = getNumberAndEndIndex(oldCoolText)

    oldCool = info[0]

    if (roundTo != 0 and oldCool % roundTo != 0):
        newCool = oldCool + (roundTo - (oldCool % roundTo)) # rounds up to the nearest roundTo
            # rounds up instead of down because, if the server is running 5 tps:
            # 0 ms is when the first tick happens, 100 ms cooldowns are delayed until the second tick
            # 200 ms is when the second tick happens, 201 ms is delayed until the third tick (at 400 ms)
    else:
        newCool = oldCool

    newCool = max(minCool, newCool)

    newCoolText = prefix + str(newCool) + oldCoolText[info[1]:]
    return (newCoolText, newCool != oldCool, newCool)

def getNumberAndEndIndex(src):
    '''
    returns (number, index of the last digit of the number)
    defaults to (0, 0) if there is no number
    '''
    start = 0
    for i in range(0, len(src)):
        if not (src[i].isdigit() or src[i] == "-"): # negative number check in case this is used for something other than cooldowns
            if (start != i): # previous character was a number
                return (int(src[start:i]), i)
            else:
                start = i + 1
                continue
        
    return (0, 0) # default return value

def printFileUpdates(fileName, updatedOccurences, whatWasUpdated):
    '''
    Function to print out updated cooldowns
    '''
    if (len(updatedOccurences) > 0):
        print(fileName + ":") # print() automatically adds a newline at the end
        for x in updatedOccurences:
            print("Updated \"" + whatWasUpdated + "\" occurence #" + str(x) + ".")
        print()

def replaceFileText(file, text):
    fo = open(file, "w")
    fo.truncate(0)
    fo.write(text)
    fo.close()


cools("*.cs", "coolDown:", 200, 0, " ")