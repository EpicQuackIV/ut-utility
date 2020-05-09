import behaviors.behavior as behavior
from items.item import GetItems
from items.itemtypes import SlotToCategory, SlotToSlotType
import utils

class WikiGenerator:

    behavs = None
    enemyDropsList = None
    dropLocations = None
    items = None

    def __init__(this, utPath):
        this.behavs = behavior.GetBehaviorsFromGlob(utPath + "/wServer/logic/db/*.cs")
        this.enemyDropsList = behavior.GetAllDrops(this.behavs)
        this.dropLocations = behavior.GetLootAndEnemyPerc(this.behavs)

        cond = lambda x: x.GodSlayer or x.Godly or x.Sacred or x.Legendary or x.Fabled or x.RT or x.Id in this.enemyDropsList
        this.items = [i for i in GetItems(utPath + "/common/resources/xmls/client/dat1.xml") if cond(i)]
        this.items.sort(key = lambda x: x.Id)

    def FormatItem(this, it):
        loc = this.dropLocations.get(it.Id, None)
        if (loc != None):
            locs = ["\nDrops from:"]
            for l in loc:
                locs.append(l[0] + ": " + str(l[1]) + "%" + utils.percentToRate(l[1]) + " chance.")
            locs.sort()
            return str(it) + "\n".join(locs) + "\n"
        else:
            return str(it) + "\nDoes not drop from enemies.\n"

    def PrintItemsToFile(this, path):
        lout = []
        for it in this.items:
            lout.append(this.FormatItem(it))

        wikiOut = "\n==================\n\n".join(lout)

        fout = open(path, "w")
        fout.write(wikiOut)
        fout.close()

    def MakeDirs(this, path):
        import os
        if (not os.path.isdir(path)):
            raise Exception("Directory does not exist: \"" + path + "\".")

        for x in SlotToCategory.items():
            if (x[1] != SlotToSlotType[x[0]]):
                os.makedirs(path + "/" + x[1] + "/" + SlotToSlotType[x[0]], exist_ok=True)
            else:
                os.makedirs(path + "/" + x[1], exist_ok=True)

    def MakeWiki(this, path):
        this.MakeDirs(path)
        for it in this.items:
            sCat = SlotToCategory[it.SlotType]
            sTyp = SlotToSlotType[it.SlotType]
            extPath = "/" + sCat if sCat == sTyp else "/" + sCat + "/" + sTyp
            itFile = utils.FormatFileName(it.Id, "txt") 

            fout = open(path + extPath + "/" + itFile, "w")
            fout.write(this.FormatItem(it))
            fout.close()

if (__name__ == "__main__"):
    wg = WikiGenerator("something/ut-core-master/server")
    #wg.PrintItemsToFile("something/ut-utility/output/xml-parser.txt")
    wg.MakeWiki("something/ut-utility/output/wiki")
