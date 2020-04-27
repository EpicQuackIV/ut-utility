

def NotImplemented(item, xml):
    pass

def Activate(item, xml):
    activateName = xml.text
    stats = {}
    for i in xml.attrib.items():
        stats[i[0]] = i[1]
    item.Data.get(xml.tag).append((activateName, stats))

def XmlTextToString(item, xml):
    item.Data.set(xml.tag, xml.text)

def XmlTextToInt(item, xml):
    val = int(xml.text)
    item.Data.set(xml.tag, val)

def XmlTextToIntHex(item, xml):
    val = int(xml.text, 16)
    item.Data.set(xml.tag, val)

def XmlTextToFloat(item, xml):
    val = float(xml.text)
    item.Data.set(xml.tag, val)

def XmlToBool(item, xml):
    item.Data.set(xml.tag, True)

xmltag2func = {
    # unused stuff
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

    "Activate": Activate,
    "ActivateOnEquip": Activate,
    "AnimatedTexture": NotImplemented,
    "ArcGap": XmlTextToFloat,
    "Backpack": XmlToBool,
    "BagType": XmlTextToInt,    
    "Class": XmlTextToString,
    "Consumable": XmlToBool,
    "Cooldown": XmlTextToFloat,
    "Description": XmlTextToString,
    "DisplayId": XmlTextToString,
    "DungeonName": XmlTextToString,
    "EffectEquip": NotImplemented,
    "ExtraTooltipData": NotImplemented,
    "Fabled": XmlToBool,
    "FabledToken": XmlToBool,
    "FameBonus": XmlTextToInt,
    "GodSlayer": XmlToBool,
    "Godly": XmlToBool,
    "HpCost": XmlTextToInt,
    "InvUse": XmlToBool,
    "Item": XmlToBool,
    "Legend": NotImplemented,
    "Legendary": XmlToBool,
    "Lootbox": XmlToBool,
    "Mask": NotImplemented,
    "MpCost": XmlTextToInt,
    "MultiPhase": XmlToBool,
    "NumProjectiles": XmlTextToInt,
    "OldSound": NotImplemented,
    "Potion": XmlToBool,
    "Projectile": NotImplemented,
    "QuestItem": XmlToBool,
    "RT": XmlToBool,
    "RateOfFire": XmlTextToFloat,
    "RemoteTexture": NotImplemented,
    "Resurrects": XmlToBool,
    "Sacred": XmlToBool,
    "Shard": XmlToBool,
    "Size": XmlTextToInt,
    "SlotType": XmlTextToInt,
    "SorMachine": XmlToBool,
    "Soulbound": XmlToBool,
    "Sound": NotImplemented,
    "Steal": NotImplemented,
    "SuccessorId": XmlTextToString,
    "SurgeCost": XmlTextToInt,
    "Tex1": XmlTextToIntHex,
    "Tex2": XmlTextToIntHex,
    "Texture": NotImplemented,
    "Tier": XmlTextToInt,
    "Treasure": XmlToBool,
    "Usable": XmlToBool,
    "feedPower": XmlTextToInt
}
