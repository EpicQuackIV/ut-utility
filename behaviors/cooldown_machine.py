import glob
    
toReplace = "coolDownOffset:"
toAdd = " "

path = "something/ut-core-master/server/wServer/logic/db/*.cs"

def getNewCool(oldCool):
    start = 0
    oc = oldCool.split(toReplace)
    asdfasdf = oc[0]
    changed = False
    for i in range(0, len(oc[1])):
        c = oc[1][i]
        if (c == " " or c == "\n"):
            start = i + 1
            continue
        elif not c.isdigit():
            if start != i:
                #print(start, i)
                fullNum = int(oc[1][start:i])
                if fullNum < 200:# and fullNum != 0:
                    #fullNum = 200
                    changed = True
                asdfasdf += toReplace + toAdd + str(fullNum) + oc[1][i:]
            break
    if (changed):
        return (asdfasdf, True)

    return (oldCool, False)
#
#   BEGINNING OF GETNEWCOOL2
#
def getNewCool2(oldCool, storage):
    start = 0
    oc = oldCool.split(toReplace)
    asdfasdf = oc[0]
    changed = False
    val = 0
    for i in range(0, len(oc[1])):
        c = oc[1][i]
        if (c == " " or c == "\n"):
            start = i + 1
            continue
        elif not c.isdigit():
            if start != i:
                #print(start, i)
                fullNum = int(oc[1][start:i])
                pr = storage.prev()
                if (fullNum - pr < 200 and pr - fullNum < 200 and fullNum != 0):
                    fullNum += (200 - (fullNum % 200))
                    changed = True
                val = fullNum
                asdfasdf += toReplace + toAdd + str(fullNum) + oc[1][i:]
            break

    if (changed):
        return (asdfasdf, True, val)

    return (oldCool, False, val)


def cools1():
    for fileName in glob.glob(path):
        lines = []
        fo = open(fileName, "r")
        fileArr = fo.readlines()
        fo.close()

        #fileArr = fileStr.split(toReplace)

        for x in range(1, len(fileArr)):
            cool = fileArr[x]
            if (cool.count(toReplace) > 0):
                #print("lmao")
                newCool = getNewCool(cool)
                if (newCool[1]):
                    lines.append((x + 1, newCool[0]))
                    fileArr[x] = newCool[0]

        if (len(lines) > 0):
            print(fileName[fileName.find(".") + 1:])
            for aj in lines:
                print(str(aj[0]) + " " + aj[1])
            #print(str(lines) + "\n")
'''
        fo = open("BehaviorDb." + fileName + ".cs", "w")
        fo.truncate(0)
        for ez in fileArr:
            fo.write(ez)
        fo.close()'''


def cools2():
    '''
    for coolDownOffset spirals
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

'''
        fo = open("BehaviorDb." + fileName + ".cs", "w")
        fo.truncate(0)
        for ez in fileArr:
            fo.write(ez)
        fo.close()'''


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


cools1()