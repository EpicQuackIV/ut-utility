
def _InvalidTag(item, xml):
    print(item.Id + " has an unhandled XML tag: \"" + xml.tag + "\"")

def _XmlToActivate(item, xml):
    activateName = xml.text
    stats = {}
    for i in xml.attrib.items():
        stats[i[0]] = i[1]
    item.get(xml.tag).append((activateName, stats))

def _XmlTextToString(item, xml):
    item.set(xml.tag, xml.text)

def _XmlTextToInt(item, xml):
    val = int(xml.text, 0) # automatically switches to base 16 if it starts with "0x"
    item.set(xml.tag, val)

def _XmlTextToFloat(item, xml):
    val = float(xml.text)
    item.set(xml.tag, val)

def _XmlToBool(item, xml):
    item.set(xml.tag, True)

_XmlTagToFunc = {
    # xml tags that aren't used for anything in the game, or are only on items that aren't obtainable
    "Ascended": NotImplemented,
    "CrateLoot": NotImplemented,
    "Doses": NotImplemented,
    "EnchantMaterial": NotImplemented,
    "Enchantable": NotImplemented,
    "Enchanter": NotImplemented,
    "Outfit": NotImplemented,
    "PetFamily": NotImplemented,
    "PetId": NotImplemented,
    "PetSkin": NotImplemented,
    "PetStone": NotImplemented,
    "PlayerExclusive": NotImplemented,
    "Rarity": NotImplemented,
    "ScaleValue": NotImplemented,
    "Shop": NotImplemented,
    "Timer": NotImplemented,
    "Track": NotImplemented,
    "Undead": NotImplemented,
    "VaultItem": NotImplemented,
    "XpBoost": NotImplemented,

    # stuff that isn't supposed to be in object's xml
    #"Amplitude": NotImplemented,
    #"ArmorPierce": NotImplemented,
    #"ArmorPiercing": NotImplemented,
    #"Boomerang": NotImplemented,
    #"CondChance": NotImplemented,
    #"ConditionEffect": NotImplemented,
    #"DisplayID": NotImplemented,
    #"ExtraToolTipData": NotImplemented,
    #"Frequency": NotImplemented,
    #"MpEndCost": NotImplemented,
    #"QD": NotImplemented,
    #"Sc": NotImplemented,

    "Activate": _XmlToActivate,
    "ActivateOnEquip": _XmlToActivate,
    "AnimatedTexture": NotImplemented,
    "ArcGap": _XmlTextToFloat,
    "Backpack": _XmlToBool,
    "BagType": _XmlTextToInt,    
    "Class": _XmlTextToString,
    "Consumable": _XmlToBool,
    "Cooldown": _XmlTextToFloat,
    "Description": _XmlTextToString,
    "DisplayId": _XmlTextToString,
    "DungeonName": _XmlTextToString,
    "EffectEquip": NotImplemented,
    "ExtraTooltipData": NotImplemented,
    "Fabled": _XmlToBool,
    "FabledToken": _XmlToBool,
    "FameBonus": _XmlTextToInt,
    "GodSlayer": _XmlToBool,
    "Godly": _XmlToBool,
    "HpCost": _XmlTextToInt,
    "InvUse": _XmlToBool,
    "Item": _XmlToBool,
    "Legend": NotImplemented,
    "Legendary": _XmlToBool,
    "Lootbox": _XmlToBool,
    "Mask": NotImplemented,
    "MpCost": _XmlTextToInt,
    "MultiPhase": _XmlToBool,
    "NumProjectiles": _XmlTextToInt,
    "OldSound": NotImplemented,
    "Potion": _XmlToBool,
    "Projectile": NotImplemented,
    "QuestItem": _XmlToBool,
    "RT": _XmlToBool,
    "RateOfFire": _XmlTextToFloat,
    "RemoteTexture": NotImplemented,
    "Resurrects": _XmlToBool,
    "Sacred": _XmlToBool,
    "Shard": _XmlToBool,
    "Size": _XmlTextToInt,
    "SlotType": _XmlTextToInt,
    "SorMachine": _XmlToBool,
    "Soulbound": _XmlToBool,
    "Sound": NotImplemented,
    "Steal": NotImplemented,
    "SuccessorId": _XmlTextToString,
    "SurgeCost": _XmlTextToInt,
    "Tex1": _XmlTextToInt,
    "Tex2": _XmlTextToInt,
    "Texture": NotImplemented,
    "Tier": _XmlTextToInt,
    "Treasure": _XmlToBool,
    "Usable": _XmlToBool,
    "feedPower": _XmlTextToInt
}


def SetElementData(item, xml):
    _XmlTagToFunc.get(xml.tag, _InvalidTag)(item, xml)
