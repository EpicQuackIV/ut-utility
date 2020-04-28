import glob

#######################################################
#                                                     #
#  The Cooldown Machine, for fixing broken cooldowns  #
#                                                     #
#######################################################

toReplace = "coolDown:" # what behavior parameters it checks numbers for
minCool = 200 # the minimum allowable cooldown
toAdd = " " # adds a space between toReplace and the new cooldown
prefix = toReplace + toAdd

path = "*.cs" # or "something/server/wServer/logic/db/*.cs"

def getNewCool(oldCool):
    '''
    Increases a cooldown from less than minCool to minCool
    oldCool must be a string that begins with an int. There can be whitespace before the int.
    returns (int cooldown, bool was_cooldown_changed)
    '''
    info = getNumberAndEndIndex(oldCool)
    newCool = prefix
    if (info[0] < minCool): # if old cooldown is less than minimum new cooldown then replace it
        newCool += str(minCool) + oldCool[info[1]:]
        return (newCool, True)
    else: # don't change the cooldown
        newCool += str(info[0]) + oldCool[info[1]:]
        return (newCool, False)


def getNewCool2(oldCool, storage):
    '''
    Fixes spiral shooting behaviors that use Shoot() with different coolDownOffset values
    A spiral with coolDownOffsets of 0, 100, 200, 300, 450, 460, 600 will be changed to 0, 200, 200, 400, 600, 600, 600
    '''
    oc = oldCool.split(toReplace)
    newCool = oc[0]
    changed = False
    val = 0
    for i in range(0, len(oc[1])):
        c = oc[1][i]
        if (c == " " or c == "\n"):
            start = i + 1
            continue
        elif not c.isdigit():
            if start != i:
                fullNum = int(oc[1][start:i])
                pr = storage.prev()
                if (fullNum - pr < 200 and pr - fullNum < 200 and fullNum != 0):
                    fullNum += (200 - (fullNum % 200))
                    changed = True
                val = fullNum
                newCool += toReplace + toAdd + str(fullNum) + oc[1][i:]
            break

    if (changed):
        return (newCool, True, val)

    return (oldCool, False, val)


def cools1():
    for fileName in glob.glob(path):
        updates = []
        fo = open(fileName, "r")
        fileArr = fo.read().split(toReplace)
        fo.close()

        for x in range(1, len(fileArr)):
            cool = fileArr[x]
            newCool = getNewCool(cool)
            fileArr[x] = newCool[0]
            if (newCool[1]):
                updates.append(x)

        fileDispName = fileName[fileName.rfind("/") + 1:]
        newFileText = "".join(fileArr)
        printFileUpdates(fileDispName, updates)
        replaceFileText(fileName, newFileText)


def cools2():
    '''
    #################  Currently broken, do not use #################
    Fixes spiral shooting behaviors that use Shoot() with different coolDownOffset values
    A spiral with coolDownOffsets of 0, 100, 200, 300, 450, 460, 600 will be changed to 0, 200, 200, 400, 600, 600, 600
    '''
    for fileName in glob.glob(path):
        storage = fileLineStorage()
        lines = []
        fo = open(fileName, "r")
        fileArr = fo.readlines()
        fo.close()

        #fileArr = fileStr.split(toReplace)

        for x in range(1, len(fileArr)):
            cool = fileArr[x]
            if (cool.count(toReplace) > 0):
                #print("lmao")
                newCool = getNewCool2(cool, storage)
                storage.addInfo(newCool[2])
                if (newCool[1]):
                    lines.append((x + 1, newCool[0]))
                    fileArr[x] = newCool[0]

        if (len(lines) > 0):
            print(fileName[fileName.find("."):])
            for aj in lines:
                print(str(aj[0]) + " " + aj[1])
            #print(str(lines) + "\n")

        output = "".join(fileArr)
        fo = open("BehaviorDb." + fileName + ".cs", "w")
        fo.truncate(0)
        fo.write(output)
        fo.close()


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


cools2()