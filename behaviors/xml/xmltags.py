
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
    # item.set("Texture", Texture(xml))
    pass

def _XmlToEffectEquip(item, xml):
    # item.set("EffectEquip", EffectEquip(xml))
    # or add this to ActivateOnEquip
    pass

def _XmlToExtraTooltipData(item, xml):
    # item.set("ExtraTooltipData", ExtraTooltipData(xml))
    pass

def _XmlToLegend(item, xml):
    item.set("LegendID", int(xml.attrib["id"]))

def _XmlToProjectile(item, xml):
    # item.set("Projectile", Projectile(xml))
    pass

def _XmlToSacred(item, xml):
    item.set("Sacred", True)
    item.set("SacredDesc", int(xml.attrib["desc"]))

def _XmlToSteal(item, xml):
    if (xml.attrib["type"] == "life"):
        item.set("LifeSteal", item.get("LifeSteal") + int(xml.attrib["amount"]))
    elif (xml.attrib["type"] == "mana"):
        item.set("ManaSteal", item.get("ManaSteal") + int(xml.attrib["amount"]))

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
