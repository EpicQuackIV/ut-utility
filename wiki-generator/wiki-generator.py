import behaviors.behavior as behavior
from items.item import GetItems
from utils import formatOutput

path = "something"

if (__name__ == "__main__"):
    behavs = behavior.GetBehaviorsFromGlob(path + "/ut-core-master/server/wServer/logic/db/*.cs")
    enemyDropsList = behavior.GetAllDrops(behavs)
    dropLocations = behavior.GetLootAndEnemyPerc(behavs)
    cond = lambda x: x.GodSlayer or x.Godly or x.Sacred or x.Legendary or x.Fabled or x.RT or x.Id in enemyDropsList
    items = [i for i in GetItems(path + "/ut-core-master/server/common/resources/xmls/client/dat1.xml") if cond(i)]

    items.sort(key = lambda x: x.Id)
    wikiOut = formatOutput(items, dropLocations)

    fout = open(path + "/ut-utility/output/xml-parser.txt", "r+")
    fout.truncate(0)
    fout.write(wikiOut)
    fout.close()

