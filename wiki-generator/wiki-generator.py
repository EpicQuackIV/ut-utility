import behaviors.behavior as behavior
from items.item import GetItems

path = "something"

behavs = behavior.GetBehaviorsFromGlob(path + "/ut-core-master/server/wServer/logic/db/*.cs")
behavsItemList = behavior.GetAllDrops(behavs)

cond = lambda x: x.Sacred or x.Legendary or x.RT
items = [i for i in GetItems(path + "/ut-core-master/server/common/resources/xmls/client/dat1.xml")]


fout = open(path + "/ut-utility/output/xml-parser.txt", "r+")
fout.truncate(0)
lout = [str(i) for i in items if cond(i)]
lout.sort()
fout.write("\n==================\n\n".join(lout))
fout.close()
