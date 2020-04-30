
def _InvalidTag(item, xml):
    print(item.Id + " has an unhandled XML tag: \"" + xml.tag + "\"")

def _NotImplemented(item, xml):
    pass

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
    "AnimatedTexture": _NotImplemented,
    "ArcGap": _XmlTextToFloat,
    "Backpack": _XmlToBool,
    "BagType": _XmlTextToInt,    
    "Class": _XmlTextToString,
    "Consumable": _XmlToBool,
    "Cooldown": _XmlTextToFloat,
    "Description": _XmlTextToString,
    "DisplayId": _XmlTextToString,
    "DungeonName": _XmlTextToString,
    "EffectEquip": _NotImplemented,
    "ExtraTooltipData": _NotImplemented,
    "Fabled": _XmlToBool,
    "FabledToken": _XmlToBool,
    "FameBonus": _XmlTextToInt,
    "GodSlayer": _XmlToBool,
    "Godly": _XmlToBool,
    "HpCost": _XmlTextToInt,
    "InvUse": _XmlToBool,
    "Item": _XmlToBool,
    "Legend": _NotImplemented,
    "Legendary": _XmlToBool,
    "Lootbox": _XmlToBool,
    "Mask": _NotImplemented,
    "MpCost": _XmlTextToInt,
    "MultiPhase": _XmlToBool,
    "NumProjectiles": _XmlTextToInt,
    "OldSound": _NotImplemented,
    "Potion": _XmlToBool,
    "Projectile": _NotImplemented,
    "QuestItem": _XmlToBool,
    "RT": _XmlToBool,
    "RateOfFire": _XmlTextToFloat,
    "RemoteTexture": _NotImplemented,
    "Resurrects": _XmlToBool,
    "Sacred": _XmlToBool,
    "Shard": _XmlToBool,
    "Size": _XmlTextToInt,
    "SlotType": _XmlTextToInt,
    "SorMachine": _XmlToBool,
    "Soulbound": _XmlToBool,
    "Sound": _NotImplemented,
    "Steal": _NotImplemented,
    "SuccessorId": _XmlTextToString,
    "SurgeCost": _XmlTextToInt,
    "Tex1": _XmlTextToInt,
    "Tex2": _XmlTextToInt,
    "Texture": _NotImplemented,
    "Tier": _XmlTextToInt,
    "Treasure": _XmlToBool,
    "Usable": _XmlToBool,
    "feedPower": _XmlTextToInt
}


def SetElementData(item, xml):
    _XmlTagToFunc.get(xml.tag, _InvalidTag)(item, xml)
