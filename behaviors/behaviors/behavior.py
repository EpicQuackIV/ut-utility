'''
Behavior(host)
Behavior.Load(src)
TrimLine(src)

string host
Dictionary<string, string> behaviors
List<string> states
List<string> transitions
'''
import utils as u
from glob import glob
class Behavior:

    host = ""
    behaviors = []
    states = []
    transitions = []

    def __init__(this, hostBehav):
        '''Sets the behavior's host variable.'''
        this.behaviors = []
        this.states = []
        this.transitions = []
        this.host = u.firstString(hostBehav)
        this.Load(hostBehav)

    def Load(this, src):
        '''Fills the behaviors, states, and transitions variables based on the src parameter.'''
        tLine = ""
        sLine = ""
        lines = src.split("\n")
        for line in lines:
            tLine = TrimBehaviorLine(line)
            if (len(tLine) == 0):
                continue
            sLine = u.beforeFirst(tLine, "(").strip(" ")
            if (len(sLine) == 0):
                return
            elif sLine.lower().find("state") != -1:
                this.states.append(u.firstString(tLine))
            elif sLine.lower().find("transition") != -1:
                this.transitions.append(sLine)
            else:
                dats = u.firstString(tLine)
                dats2 = u.firstNumber(u.afterFirst(tLine, dats))
                if (len(dats) > 0 or dats2 > 0):# and dats.find("Potion") == -1):
                    this.behaviors.append((sLine, (dats, dats2)))

    def BehaviorsOfType(this, bType):
        '''Returns a list of values from this object's behavior dictionary where the key equals the bType parameter and the value is not empty.'''
        return [x[1] for x in this.behaviors if x[0] == bType]

def TrimBehaviorLine(src):
    '''Returns an empty string or a string starting at the behavior's name.'''
    if (u.beforeFirst(src, "new ").find("//") != -1):
        return ""
    return u.afterFirst(src, "new ")

def GetBehaviors(src):
    '''Returns an array of behaviors, parsed from the src parameter.'''
    from behavior import Behavior
    ret = []
    behavs = src.split(".Init")[1:]
    for enemyBehav in behavs:
        behav = Behavior(enemyBehav)
        ret.append(behav)
    return ret

def GetBehaviorsFromGlob(globSrc):
    '''Returns an array containing every behavior from every file in the globSrc parameter.'''
    ret = []
    for fileName in glob(globSrc):
        print (u.afterFirst(fileName, "."))
        fo = open(fileName)
        fileText = fo.read()
        fo.close()
        ret.extend(GetBehaviors(fileText))
    return ret

def GetLootAndPerc(behavs, excludeCondition):
    '''
    Params: Behavior[] behavs, predicate<Tuple<string, float>> excludeCondition
    Returns: string
    Returns a formatted string containing a list of enemies, loot, and drop chances. Does not include loots where excludeCondition(loot) is True.
    '''
    ret = ""

    for behav in behavs:
        #select only itemloot behaviors
        loots = behav.BehaviorsOfType("ItemLoot");
        # add and format the enemy's name and loot to  the output string
        if len(loots) == 0:
            continue
        shortList = ""
        loots.sort()
        for loot in loots:
            if excludeCondition(loot):
                continue
            shortList += "\t" + loot[0] + ", " + str(round(loot[1] * 100, 3)) + "%\n"

        if shortList != "":
            bigList += behav.host + ":\n" + shortList

    return bigList

def GetAllDrops(behavs, exclude):
    '''
    Params: Behavior[] behavs, string[] exclude
    Returns: string[]
    Returns a string[] with every item that drops in the behavs parameter and is not in the exclude parameter. No repeated items and the items are alphabetically sorted.
    '''
    ret = []
    for behav in behavs:
        #select only itemloot behaviors
        loots = behav.BehaviorsOfType("ItemLoot");
        # add and format the enemy's name and loot to  the output string
        if len(loots) == 0:
            continue
        for loot in loots:
            if loot[0] in exclude or loot[0] in ret:
                continue
            ret.append(loot[0])
    ret.sort()
    return ret

