from itemtypes import SlotToCategory


def _InvalidTag(item, xml):
    print(item.Id + " has an unhandled XML tag: \"" + xml.tag + "\"")

def _NotImplemented(item, xml):
    pass


class Texture():

    Remote = False
    File = None
    Index = 0

    def __init__(this, xml):
        if (xml.tag == "RemoteTexture"):
            this.Remote = True
            this.File = xml.get("Instance")
            this.Index = int(xml.get("Id") or 0)
        else:
            this.File = xml.get("File")
            this.Index = int(xml.get("Index") or 0)


class ExtraTooltipData():

    def __init__(this, xml):
        this._data = [] # List<Tuple<string, string>>

        for x in xml.findall("EffectInfo"):
            this._data.append((x.get("name"), x.get("description")))

    def __str__(this):
        ret = []
        for eff in this._data:
            if (eff[0] == "" or eff[1] == ""):
                ret.append(eff[0] + eff[1])
            else:
                ret.append(eff[0] + ": " + eff[1])
        return "\n".join(ret)
 

class Projectile():

    Item = None
    ObjectId = None
    LifetimeMS = 0
    Speed = 0.0
    MinDamage = 0
    MaxDamage = 0
    Size = 100
    Amplitude = 0.0
    Frequency = 0.0
    Magnitude = 0.0 # todo: figure out what magnitude does, if anything
    MultiHit = False
    PassesCover = False
    ArmorPiercing = False
    ParticleTrail = False
    Wavy = False
    Parametric = False
    Boomerang = False

    def __init__(this, xml):
        this.Item = None
        this.Effects = [] # List<Tuple<string, float>>
        this.CondChance = [] # List<Tuple<string, float, float>> (that's effect, duration, chance)
        this.ObjectId = xml.find("ObjectId").text
        this.LifetimeMS = int(xml.find("LifetimeMS").text)
        this.Speed = float(xml.find("Speed").text)

        x = xml.find("Damage")
        if (x != None):
            this.MinDamage = int(x.text)
            this.MaxDamage = this.MinDamage
        else:
            this.MinDamage = int(xml.find("MinDamage").text)
            this.MaxDamage = int(xml.find("MaxDamage").text)

        x = xml.find("Size")
        if (x != None):
            this.Size = int(x.text)
        x = xml.find("Amplitude")
        if (x != None):
            this.Amplitude = float(x.text)
        x = xml.find("Frequency")
        if (x != None):
            this.Frequency = float(x.text)
        x = xml.find("Magnitude")
        if (x != None):
            this.Magnitude = float(x.text)

        if (xml.find("MultiHit") != None):
            this.MultiHit = True
        if (xml.find("PassesCover") != None):
            this.PassesCover = True
        if (xml.find("ArmorPiercing") != None):
            this.ArmorPiercing = True
        if (xml.find("ParticleTrail") != None):
            this.ParticleTrail = True
        if (xml.find("Wavy") != None):
            this.Wavy = True
        if (xml.find("Parametric") != None):
            this.Parametric = True
        if (xml.find("Boomerang") != None):
            this.Boomerang = True

        for eff in xml.findall("ConditionEffect"):
            this.Effects.append((eff.text, float(eff.get("duration"))))

        for cond in xml.findall("CondChance"):
            this.CondChance.append((cond.get("effect"), float(cond.get("duration")), float(cond.get("chance"))))

    def __str__(this):
        ret = []
        ret.append("Does " + (str(this.MinDamage) if this.MinDamage == this.MaxDamage else str(this.MinDamage) + "-" + str(this.MaxDamage)) + " damage.")
        if (this.Item != None and SlotToCategory[this.Item.SlotType] == "weapon"):
            ret.append(str(int(this.Item.RateOfFire * 100)) + "% rate of fire.")
            if (this.Item.NumProjectiles > 1):
                ret.append("Shoots " + str(this.Item.NumProjectiles) + " shots at a " + str(this.Item.ArcGap) + " degree angle.")
            else:
                ret.append("Shoots 1 shot.")
        ret.append(str(round(this.Speed * this.LifetimeMS * (0.00005 if this.Boomerang else 0.0001), 2)) + " tile range.")
        if (this.Amplitude > 0):
            ret.append("Shots have an amplitude of " + str(round(this.Amplitude, 2)) + " tiles and a frequency of " + str(round(this.Frequency)) + ".")
        if (this.MultiHit):
            ret.append("Shots hit multiple targets.")
        if (this.PassesCover):
            ret.append("Shots pass through obstacles.")
        if (this.ArmorPiercing):
            ret.append("Shots ignore defense.")
        if (this.Wavy):
            ret.append("Shots are wavy.")
        if (this.Parametric):
            ret.append("Shots are parametric.")
        if (this.Boomerang):
            ret.append("Shots boomerang.")
        return "\n".join(ret)

    def setitem(this, item):
        this.Item = item


def _XmlToActivate(item, xml):
    activateName = xml.text
    stats = xml.attrib.copy()
    item.get(xml.tag).append((activateName, stats))

def _XmlToString(item, xml):
    item.set(xml.tag, xml.text)

def _XmlToInt(item, xml):
    val = int(xml.text, 0) # automatically switches to base 16 if it starts with "0x"
    item.set(xml.tag, val)

def _XmlToFloat(item, xml):
    val = float(xml.text)
    item.set(xml.tag, val)

def _XmlToBool(item, xml):
    item.set(xml.tag, True)

def _XmlToTexture(item, xml):
    # AnimatedTexture, RemoteTexture, Texture, Mask
    item.set("Texture", Texture(xml))
    pass

def _XmlToEffectEquip(item, xml):
    eff = xml.attrib.copy()
    item.get("ActivateOnEquip").append(("EffectEquip", eff))
    pass

def _XmlToExtraTooltipData(item, xml):
    item.set("ExtraTooltipData", ExtraTooltipData(xml))
    pass

def _XmlToLegend(item, xml):
    item.set("LegendID", int(xml.get("id")))

def _XmlToProjectile(item, xml):
    prj = Projectile(xml)
    prj.setitem(item)
    item.set("Projectile", prj)
    pass

def _XmlToSacred(item, xml):
    item.set("Sacred", True)
    item.set("SacredDesc", int(xml.get("desc")))

def _XmlToSteal(item, xml):
    if (xml.get("type") == "life"):
        item.set("LifeSteal", item.get("LifeSteal") + int(xml.get("amount")))
    elif (xml.get("type") == "mana"):
        item.set("ManaSteal", item.get("ManaSteal") + int(xml.get("amount")))

_XmlTagToFunc = {
    # xml tags that aren't used for anything in the game, or are only on items that aren't obtainable
    "Ascended": _NotImplemented,
    "CrateLoot": _NotImplemented,
    "Doses": _NotImplemented,
    "EnchantMaterial": _NotImplemented,
    "Enchantable": _NotImplemented,
    "Enchanter": _NotImplemented,
    "Outfit": _NotImplemented,
    "PetFamily": _NotImplemented,
    "PetId": _NotImplemented,
    "PetSkin": _NotImplemented,
    "PetStone": _NotImplemented,
    "PlayerExclusive": _NotImplemented,
    "Rarity": _NotImplemented,
    "ScaleValue": _NotImplemented,
    "Shop": _NotImplemented,
    "Timer": _NotImplemented,
    "Track": _NotImplemented,
    "Undead": _NotImplemented,
    "VaultItem": _NotImplemented,
    "XpBoost": _NotImplemented,

    # stuff that isn't supposed to be in object's xml
    #"Amplitude": _NotImplemented,
    #"ArmorPierce": _NotImplemented,
    #"ArmorPiercing": _NotImplemented,
    #"Boomerang": _NotImplemented,
    #"CondChance": _NotImplemented,
    #"ConditionEffect": _NotImplemented,
    #"DisplayID": _NotImplemented,
    #"ExtraToolTipData": _NotImplemented,
    #"Frequency": _NotImplemented,
    #"MpEndCost": _NotImplemented,
    #"QD": _NotImplemented,
    #"Sc": _NotImplemented,

    "Activate": _XmlToActivate,
    "ActivateOnEquip": _XmlToActivate,
    "AnimatedTexture": _XmlToTexture,
    "ArcGap": _XmlToFloat,
    "Backpack": _XmlToBool,
    "BagType": _XmlToInt,    
    "Class": _XmlToString,
    "Consumable": _XmlToBool,
    "Cooldown": _XmlToFloat,
    "Description": _XmlToString,
    "DisplayId": _XmlToString,
    "DungeonName": _XmlToString,
    "EffectEquip": _XmlToEffectEquip,
    "ExtraTooltipData": _XmlToExtraTooltipData,
    "Fabled": _XmlToBool,
    "FabledToken": _XmlToBool,
    "FameBonus": _XmlToInt,
    "GodSlayer": _XmlToBool,
    "Godly": _XmlToBool,
    "HpCost": _XmlToInt,
    "InvUse": _XmlToBool,
    "Item": _XmlToBool,
    "Legend": _XmlToLegend,
    "Legendary": _XmlToBool,
    "Lootbox": _XmlToBool,
    "Mask": _XmlToTexture,
    "MpCost": _XmlToInt,
    "MultiPhase": _XmlToBool,
    "NumProjectiles": _XmlToInt,
    "OldSound": _XmlToString,
    "Potion": _XmlToBool,
    "Projectile": _XmlToProjectile,
    "QuestItem": _XmlToBool,
    "RT": _XmlToBool,
    "RateOfFire": _XmlToFloat,
    "RemoteTexture": _XmlToTexture,
    "Resurrects": _XmlToBool,
    "Sacred": _XmlToSacred,
    "Shard": _XmlToBool,
    "Size": _XmlToInt,
    "SlotType": _XmlToInt,
    "SorMachine": _XmlToBool,
    "Soulbound": _XmlToBool,
    "Sound": _XmlToString,
    "Steal": _XmlToSteal,
    "SuccessorId": _XmlToString,
    "SurgeCost": _XmlToInt,
    "Tex1": _XmlToInt,
    "Tex2": _XmlToInt,
    "Texture": _XmlToTexture,
    "Tier": _XmlToInt,
    "Treasure": _XmlToBool,
    "Usable": _XmlToBool,
    "feedPower": _XmlToInt
}


def SetElementData(item, xml):
    _XmlTagToFunc.get(xml.tag, _InvalidTag)(item, xml)
