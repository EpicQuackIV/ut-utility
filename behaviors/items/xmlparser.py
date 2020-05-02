import xml.etree.ElementTree as ET
from item import Item
from itemtypes import SlotToSlotType


def GetItems(path, addCondition):
    '''
    Params: string path, predicate<Item> addCondition
    Returns: list<Item>
    Returns a dictionary of every item found in the xml file found at path if addCondition is true for that item.
    '''
    xmlData = ET.parse(path).getroot()
    ret = []
    for xml in xmlData.findall(".//Object[Item]"):
        ret.append(Item(xml))

    print (len(ret))
    return ret

cond = lambda x: x.Sacred or x.Legendary or x.RT

fout = open("something/ut-utility/output/xml-parser.txt", "r+")
itemList = GetItems("something/ut-core-master/server/common/resources/xmls/client/dat1.xml", cond)
fout.truncate(0)
lout2 = [str(i) for i in itemList if True]
#lout2.sort()
fout.write("\n==================\n\n".join(lout2))
fout.close()