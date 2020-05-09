from items.xmltags import SetElementData
from items.itemtypes import *
import xml.etree.ElementTree as ET

def GetItems(path):
    '''
    Params: string path
    Returns: list<Item>
    Returns a list of every item found in the xml file found at path.
    '''
    xmlData = ET.parse(path).getroot()
    ret = []
    for xml in xmlData.findall(".//Object[Item]"):
        ret.append(Item(xml))

    print (len(ret))
    return ret

class Item():

    Class = None # for items, this is almost always "Equipment"
    Description = None
    DisplayId = None # better to use Id to avoid language formatting like "{equip.energy_staff}"
    DungeonName = None
    OldSound = None
    Sound = None
    SuccessorId = None

    Tier = -1
    GodSlayer = False
    Godly = False
    Sacred = False
    SacredID = -1
    Legendary = False
    Legend = None
    Fabled = False
    RT = False
    Untiered = Tier == -1

    BagType = 0 # brown bag
    FameBonus = 0
    HpCost = 0
    LifeSteal = 0
    ManaSteal = 0
    MpCost = 0
    NumProjectiles = 1
    Size = 100
    SlotType = 0
    SurgeCost = 0
    Tex1 = 0
    Tex2 = 0
    feedPower = 0

    ArcGap = 0.0
    Cooldown = 0.5
    RateOfFire = 1.0

    Backpack = False
    Consumable = False
    FabledToken = False
    InvUse = False
    Lootbox = False
    MultiPhase = False
    Potion = False
    QuestItem = False
    Resurrects = False
    Shard = False
    SorMachine = False
    Soulbound = False
    Treasure = False
    Usable = False

    ExtraTooltipData = None
    Projectile = None
    Texture = None

    def __init__(this, itemXml):
        this.Id = itemXml.get("id")
        this.ObjType = int(itemXml.get("type"), 16)
        this.Activate = [] # # List<Tuple<string, Dict<string, string>>>
        this.ActivateOnEquip = [] # List<Tuple<string, Dict<string, string>>>
        this.ExtraTooltipData = None
        this.Projectile = None
        this.Texture = None
        this.Legend = None

        for element in itemXml:
            SetElementData(this, element)

    def __str__(this):
        try:
            ret = [this.Id + " [" + hex(this.ObjType) + "]"]
            if (this.Description != None):
                ret.append("\"" + this.Description + "\"")
            ret.append(this.makeTierText()[:-1] + " " + SlotToSlotType[this.SlotType].replace("-", " ") + ".")
            if (this.Soulbound):
                ret.append("This item is soulbound.")
            if (this.Resurrects):
                ret.append("This item resurrects the player.")
            ret.append("")
            if (this.Projectile != None):
                ret.append(str(this.Projectile))
            if (this.Usable):
                ret.append(this.makeCostText())
                if (not this.Consumable):
                    ret.append("Cooldown: " + str(round(this.Cooldown, 2)) + " seconds.")
            if (this.FameBonus > 0):
                ret.append("Fame Bonus: " + str(this.FameBonus) + "%.")
            if (len(this.Activate) > 0 or len(this.ActivateOnEquip) > 0):
                ret.append(this.makeActivateText())
            if (this.LifeSteal > 0 or this.ManaSteal > 0):
                ret.append(this.makeStealText())
            if (this.ExtraTooltipData != None):
                ret.append(str(this.ExtraTooltipData))
            if (this.SacredID != -1):
                ret.append(SacredIDToDesc[this.SacredID])
            if (this.Legend != None):
                ret.append(str(this.Legend))
            newRet = "\n".join(ret).replace("\n\n\n", "\n\n")
            return newRet + ("\n" if not newRet.endswith("\n") else "")
        except Exception as e:
            return "Error when converting \"" + this.Id + "\" to string:\n" + str(e)

    def set(this, variableName, value):
        setattr(this, str(variableName), value)

    def get(this, variableName):
        return getattr(this, variableName)

    def makeActivateText(this):
        ret = []

        if (len(this.Activate) > 0):
            aes = []
            for ae in this.Activate:
                aes.append(AEFormatter.get(ae[0], lambda x: "Unknown Effect \"" + ae[0] + "\" on item \"" + this.Id + "\"")(ae[1]))
            while "" in aes:
                aes.remove("")
            if (len(aes) > 0):
                aes.sort()
                aes.insert(0, "\nWhen used:")
                ret.append("\n".join(aes))

        if (len(this.ActivateOnEquip) > 0):
            aoes = []
            for aoe in this.ActivateOnEquip:
                aoes.append(AOEFormatter.get(aoe[0], lambda x: "Unknown Effect \"" + aoe[0] + "\" on item \"" + this.Id + "\"")(aoe[1]))
            while "" in aoes:
                aoes.remove("")
            if (len(aoes) > 0):
                aoes.sort()
                aoes.insert(0, "\nWhile equipped:")
                ret.append("\n".join(aoes))

        return "\n".join(ret) + "\n" if len(ret) > 0 else ""

    def makeTierText(this):
        if (this.GodSlayer):
            return "Godslayer tier."
        elif (this.Godly):
            return "Godly tier."
        elif (this.Sacred):
            return "Sacred tier."
        elif (this.Legendary):
            return "Legendary tier."
        elif (this.Fabled):
            return "Fabled tier."
        elif (this.RT):
            return "Rusted tier."
        elif (this.Tier == -1):
            return "Untiered."
        else:
            return "Tier " + str(this.Tier) + "."

    def makeStealText(this):
        ret = []

        if (len(this.ActivateOnEquip) == 0):
            ret.append("While equipped:")
        if (this.LifeSteal > 0):
            ret.append("{:+d} Life Steal.".format(this.LifeSteal))
        if (this.ManaSteal > 0):
            ret.append("{:+d} Mana Leech.".format(this.ManaSteal))

        return "\n".join(ret) + "\n"

    def makeCostText(this):
        ret = []
        if (this.HpCost > 0):
            ret.append("HP Cost: " + str(this.HpCost) + ".")
        if (this.MpCost > 0):
            ret.append("MP Cost: " + str(this.MpCost) + ".")
        if (this.SurgeCost > 0):
            ret.append("Surge Cost: " + str(this.SurgeCost) + ".")

        return "\n".join(ret)
