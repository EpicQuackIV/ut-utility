from xmltags import SetElementData
from itemtypes import *

class Item():

    Description = None
    NumProjectiles = 0
    Tier = -1
    SlotType = 0
    GodSlayer = False
    Godly = False
    Sacred = False
    Legendary = False
    Fabled = False
    RT = False
    Shard = False

    Backpack = False
    Consumable = False
    FabledToken = False
    InvUse = False
    Lootbox = False
    MultiPhase = False
    Potion = False
    QuestItem = False
    Resurrects = False
    SorMachine = False
    Soulbound = False
    Treasure = False
    Usable = False

    def __init__(this, itemXml):
        this.Id = itemXml.attrib["id"]
        this.ObjType = int(itemXml.attrib["type"], 16)
        this.Activate = [] # # List<Tuple<string, Dict<string, string>>>
        this.ActivateOnEquip = [] # List<Tuple<string, Dict<string, string>>>

        for element in itemXml:
            SetElementData(this, element)

    def __str__(this):
        try:
            ret = [this.Id]
            ret.append("Object Type " + hex(this.ObjType))
            if (this.Description != None):
                ret.append(this.Description)
            ret.append(this.makeActivateText())
            return "\n".join(ret)
        except:
            return "\nError when converting \"" + this.Id + "\" to string.\n"

    def set(this, variableName, value):
        setattr(this, str(variableName), value)

    def get(this, variableName):
        return getattr(this, variableName)

    def makeActivateText(this):
        ret = []

        if (len(this.ActivateOnEquip) > 0):
            aoes = []
            for aoe in this.ActivateOnEquip:
                aoes.append(AOEFormatter.get(aoe[0], lambda x: "Unknown Effect \"" + aoe[0] + "\" on item \"" + this.Id + "\"")(aoe[1]))
            aoes.sort()
            aoes.insert(0, "While equipped:")
            ret.append("\n".join(aoes))

        if (len(this.Activate) > 0):
            aes = []
            for ae in this.Activate:
                aes.append(AEFormatter.get(ae[0], lambda x: "Unknown Effect \"" + ae[0] + "\" on item \"" + this.Id + "\"")(ae[1]))
            aes.sort()
            aes.insert(0, "When used:")
            ret.append("\n".join(aes))

        return "\n".join(ret)