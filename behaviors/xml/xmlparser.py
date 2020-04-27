import xml.etree.ElementTree as ET
from itemtypes import *#slot2type


def GetItems(path, addCondition):
    '''
    Params: string path, predicate<Item> addCondition
    Returns: list<Item>
    Returns a dictionary of every item found in the xml file found at path if addCondition() is true for that item.
    '''
    xmlData = ET.parse(path).getroot()
    ret = []
    for xml in xmlData.findall(".//Object[Item]"):
        y = Item(xml)

        if (addCondition(y)):
            ret.append(y)

    print (len(ret))
    ret.sort(key=lambda abc: abc.Id)
    return ret

floot = open("something/ut-utility/output/loot-list.txt", "r")
allowedItems = floot.read()
floot.close()
allowedItems.split("\n")

cond = lambda x: x.Data.Sacred or x.Data.Legendary or x.Data.RT or (x.Id in allowedItems and x.Data.Tier == 0 and slot2category[x.Data.SlotType] != "consumable")

cond2 = lambda x: x.Data.RT

def f(x):
    sName = slot2slotname[x.Data.SlotType]
    sName = sName.replace("-", " ")
    sName = sName.capitalize()
    return "[ " + sName + " ] : " + x.Id

fout = open("something/ut-utility/output/xml-parser.txt", "r+")
lout = GetItems("something/ut-core-master/server/common/resources/xmls/client/dat1.xml", cond)
fout.truncate(0)
lout2 = [i.Id for i in lout if True]
lout2.sort()
fout.write("\n".join(lout2))
fout.close()
