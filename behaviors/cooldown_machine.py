import glob

# Note: Don't use this on behavior files that won't compile

#######################################################
#                                                     #
#  The Cooldown Machine, for fixing broken cooldowns  #
#                                                     #
#######################################################

toReplace = "coolDown:" # which behavior parameter it checks numbers of
roundTo = 200 # the number to round to
toAdd = " " # adds a space between toReplace and the new cooldown
prefix = toReplace + toAdd

path = "*.cs" # or "something/server/wServer/logic/db/*.cs"

def getNewCool(oldCool, minNum, shouldRound):
    '''
    Sets everything to multiples of roundTo. Useful for getting rid of weird numbers
    Sets negative numbers to 0
    '''
    info = getNumberAndEndIndex(oldCool)

    oldNum = info[0]

    if (shouldRound):
        newNum = oldNum + (roundTo - (oldNum % roundTo)) # rounds up to the nearest roundTo
            # rounds up instead of down because, if the server is running 5 tps:
            # 0 ms is when the first tick happens, 100 ms cooldowns are delayed until the second tick
            # 200 ms is when the second tick happens, 201 ms is delayed until the third tick (at 400 ms)
    else:
        newNum = oldNum

    newNum = max(minNum, newNum)

    newCool = prefix + str(newNum) + oldCool[info[1]:]
    return (newCool, newNum != oldNum, newNum)

def cools(minNum, shouldRound):
    for fileName in glob.glob(path):
        updates = []
        fo = open(fileName, "r")
        fileArr = fo.read().split(toReplace)
        fo.close()

        for x in range(1, len(fileArr)):
            cool = fileArr[x]
            newCool = getNewCool(cool, minNum, shouldRound)
            fileArr[x] = newCool[0]
            if (newCool[1]):
                updates.append(x)

        fileDispName = fileName[fileName.rfind("/") + 1:]
        newFileText = "".join(fileArr)
        printFileUpdates(fileDispName, updates)
        replaceFileText(fileName, newFileText)

class fileLineStorage:
    linesInfo = []
    lineNum = 0

    def __init__(this):
        this.linesInfo = [0]
        this.lineNum = 0

    def addInfo(this, val):
        this.linesInfo.append(val)
        this.lineNum += 1

    def prev(this):
        return this.linesInfo[-1]

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

def printFileUpdates(fileName, updates):
    if (len(updates) > 0):
        print(fileName + ":") # print() automatically adds a newline at the end
        for x in updates:
            print("Updated \"" + toReplace + "\" occurence #" + str(x) + ".")
        print()

def replaceFileText(file, text):
    fo = open(file, "w")
    fo.truncate(0)
    fo.write(text)
    fo.close()


cools(5, False)