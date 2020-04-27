from xmltags import xmltag2func

class Item():

    def __init__(this, itemXml):
        this.Id = itemXml.attrib["id"]
        this.ObjType = int(itemXml.attrib["type"], 16)
        this.Data = ItemData()

        for element in itemXml:
            xmltag2func.get(element.tag, TagNotFound)(this, element)

    def __str__(this):
        try:
            ret = this.Id + "\n"
            ret += "Object Type " + hex(this.ObjType) + "\n"
            ret += this.Data.Description + "\n" if this.Data.Description else ""
            if (this.Data.ActivateOnEquip):
                ret += "\nWhile equipped:\n"
                aes = []
                for ae in this.Data.ActivateOnEquip:
                    aes.append(aoeformatter.get(ae[0], lambda x: "Unknown AE \"" + ae[0] + "\" on item \"" + this.Id + "\"")(ae[1]))
                aes.sort()
                ret += "\n".join(aes) + "\n"

            if (this.Data.Activate):
                ret += "\nWhen used:\n"
                aes = []
                for ae in this.Data.Activate:
                    aes.append(aeformatter.get(ae[0], lambda x: "Unknown AE \"" + ae[0] + "\" on item \"" + this.Id + "\"")(ae[1]))
                aes.sort()
                ret += "\n".join(aes) + "\n"
            return ret
        except:
            return "Error when converting \"" + this.Id + "\" to string.\n"

def TagNotFound(item, xml):
    print(item.Id + " has an unhandled XML tag: \"" + xml.tag + "\"")

class ItemData:

    Description = ""
    NumProjectiles = 0
    Tier = 0
    SlotType = 0
    Sacred = False
    Legendary = False
    RT = False

    def __init__(this):
        # initialize empty dictionaries/lists for this instance here
        this.Activate = [] # # List<Tuple<string, Dict<string, string>>>
        this.ActivateOnEquip = [] # List<Tuple<string, Dict<string, string>>>
        pass

    def set(this, variableName, value):
        exec("this." + str(variableName) + "=" + repr(value))

    def get(this, variableName):
        '''
        Only use this for variables that do not have a class (static) instance.
        '''
        return eval("this." + str(variableName))

slot2category = {
    1 : "weapon", # sword
    2 : "weapon", # dagger
    3 : "weapon", # bow
    4 : "ability", # tome
    5 : "ability", # shield
    6 : "armor", # leather-armor
    7 : "armor", # heavy-armor
    8 : "weapon", # wand
    9 : "accessory", # ring
    10: "consumable", # consumable
    11: "ability", # spell
    12: "ability", # seal
    13: "ability", # cloak
    14: "armor", # robe
    15: "ability", # quiver
    16: "ability", # helm
    17: "weapon", # staff
    18: "ability", # poison
    19: "ability", # skull
    20: "ability", # trap
    21: "ability", # orb
    22: "ability", # prism
    23: "ability", # scepter
    24: "weapon", # katana
    25: "ability", # shuriken
    26: "consumable", # pet-egg
    27: "ability", # sheath
    28: "abilty", # banner
    29: "weapon", # lance
    30: "ability", # siphon
    31: "ability", # turret
    32: "ability", # charm
    33: "ability", # dice
    34: "weapon", # blades
    35: "ability", # jacket
    36: "ability" # talisman
}

slot2slotname = {
    1 : "sword",
    2 : "dagger",
    3 : "bow",
    4 : "tome",
    5 : "shield",
    6 : "leather-armor",
    7 : "heavy-armor",
    8 : "wand",
    9 : "ring",
    10: "consumable",
    11: "spell",
    12: "seal",
    13: "cloak",
    14: "robe",
    15: "quiver",
    16: "helm",
    17: "staff",
    18: "poison",
    19: "skull",
    20: "trap",
    21: "orb",
    22: "prism",
    23: "scepter",
    24: "katana",
    25: "shuriken",
    26: "pet-egg",
    27: "sheath",
    28: "banner",
    29: "lance",
    30: "siphon",
    31: "turret",
    32: "charm",
    33: "dice",
    34: "blades",
    35: "jacket",
    36: "talisman"
}

statid2name = {
    0: "Maximum HP",
    2: "Surge",
    3: "Maximum MP",
    20: "Attack",
    21: "Defense",
    22: "Speed",
    26: "Vitality",
    27: "Wisdom",
    28: "Dexterity",
    102: "Fortune",
    110: "Surge",
    112: "Might",
    114: "Luck",
    121: "Restoration",
    122: "Protection",
    "0": "Maximum HP",
    "2": "Surge",
    "3": "Maximum MP",
    "20": "Attack",
    "21": "Defense",
    "22": "Speed",
    "26": "Vitality",
    "27": "Wisdom",
    "28": "Dexterity",
    "102": "Fortune",
    "110": "Surge",
    "112": "Might",
    "114": "Luck",
    "121": "Restoration",
    "122": "Protection",
}

statName = lambda x: statid2name.get(x, "unknown stat")
wisMod = lambda x: "Uses wis mod." if x.get("useWisMod", "") == "true" else "Does not use wis mod."

# Always capitalize the sentence and put punctuation at the end.
aeformatter = {
    "AbbyConstruct": lambda x: "Activated effect not yet implemented.",
    "ActivateFragment": lambda x: "Activated effect not yet implemented.",
    "AnguishofDrannol": lambda x: "Activated effect not yet implemented.",
    "AscensionActivate": lambda x: "Activated effect not yet implemented.",
    "AsiHeal": lambda x: "Activated effect not yet implemented.",
    "AsiimovBox": lambda x: "Activated effect not yet implemented.",
    "AstonAbility": lambda x: "Activated effect not yet implemented.",
    "Backpack": lambda x: "Activated effect not yet implemented.",
    "Banner": lambda x: "Activated effect not yet implemented.",
    "Belt": lambda x: "Activated effect not yet implemented.",
    "BigStasisBlast": lambda x: "Activated effect not yet implemented.",
    "BlackScroll": lambda x: "Activated effect not yet implemented.",
    "BlizzardBox": lambda x: "Activated effect not yet implemented.",
    "BronzeLockbox": lambda x: "Activated effect not yet implemented.",
    "BrownScroll": lambda x: "Activated effect not yet implemented.",
    "BuildTower": lambda x: "Activated effect not yet implemented.",
    "BulletNova": lambda x: "Activated effect not yet implemented.",
    "BulletNova2": lambda x: "Activated effect not yet implemented.",
    "BurningLightning": lambda x: "Activated effect not yet implemented.",
    "BurstInferno": lambda x: "Activated effect not yet implemented.",
    "ChangeSkin": lambda x: "Activated effect not yet implemented.",
    "ChristmasPopper": lambda x: "Activated effect not yet implemented.",
    "ClearConditionEffectAura": lambda x: "Activated effect not yet implemented.",
    "ClearConditionEffectSelf": lambda x: "Activated effect not yet implemented.",
    "ConditionEffectAura": lambda x: "Activated effect not yet implemented.",
    "ConditionEffectSelf": lambda x: "Activated effect not yet implemented.",
    "Create": lambda x: "Activated effect not yet implemented.",
    "CreateGauntlet": lambda x: "Activated effect not yet implemented.",
    "CreatePet": lambda x: "Activated effect not yet implemented.",
    "CrimsonBox": lambda x: "Activated effect not yet implemented.",
    "DDiceActivate": lambda x: "Activated effect not yet implemented.",
    "DamageNova": lambda x: "Activated effect not yet implemented.",
    "DareFistBox": lambda x: "Activated effect not yet implemented.",
    "DazeBlast": lambda x: "Activated effect not yet implemented.",
    "Decoy": lambda x: "Activated effect not yet implemented.",
    "Dice": lambda x: "Activated effect not yet implemented.",
    "DiceActivate": lambda x: "Activated effect not yet implemented.",
    "Drake": lambda x: "Activated effect not yet implemented.",
    "DreamEssenceActivate": lambda x: "Activated effect not yet implemented.",
    "DualShoot": lambda x: "Activated effect not yet implemented.",
    "Dye": lambda x: "Activated effect not yet implemented.",
    "EffectRandom": lambda x: "Activated effect not yet implemented.",
    "FUnlockPortal": lambda x: "Unlocks a {}.".format(x["lockedName"]),
    "Fame": lambda x: "Activated effect not yet implemented.",
    "FameActivate": lambda x: "Activated effect not yet implemented.",
    "FixedStat": lambda x: "Activated effect not yet implemented.",
    "GPBox": lambda x: "Activated effect not yet implemented.",
    "GenericActivate": lambda x: "Activated effect not yet implemented.",
    "Gift": lambda x: "Activated effect not yet implemented.",
    "Halo": lambda x: "Activated effect not yet implemented.",
    "Heal": lambda x: "Activated effect not yet implemented.",
    "Heal2": lambda x: "Activated effect not yet implemented.",
    "HealNova": lambda x: "Heals {} HP within {} tiles. {}".format(x["amount"], float(x["range"]), wisMod(x)),
    "HealNovaSigil": lambda x: "Activated effect not yet implemented.",
    "HealingGrenade": lambda x: "Activated effect not yet implemented.",
    "HeldEffect": lambda x: "Activated effect not yet implemented.",
    "IdScroll": lambda x: "Activated effect not yet implemented.",
    "IncrementStat": lambda x: "Permanently increases {} by {}.".format(statName(x["stat"]), x["amount"]),
    "InsigniaActivate": lambda x: "Activated effect not yet implemented.",
    "JacketAbility": lambda x: "Activated effect not yet implemented.",
    "JacketAbility2": lambda x: "Activated effect not yet implemented.",
    "LDBoost": lambda x: "Activated effect not yet implemented.",
    "LTBoost": lambda x: "Activated effect not yet implemented.",
    "Lightning": lambda x: "Activated effect not yet implemented.",
    "LootboxActivate": lambda x: "Activated effect not yet implemented.",
    "Magic": lambda x: "Activated effect not yet implemented.",
    "Magic2": lambda x: "Activated effect not yet implemented.",
    "MagicNova": lambda x: "Activated effect not yet implemented.",
    "MarksActivate": lambda x: "Activated effect not yet implemented.",
    "MayhemBox": lambda x: "Activated effect not yet implemented.",
    "MiniPot": lambda x: "Activated effect not yet implemented.",
    "MonsterToss": lambda x: "Activated effect not yet implemented.",
    "MultiDecoy": lambda x: "Activated effect not yet implemented.",
    "Mushroom": lambda x: "Activated effect not yet implemented.",
    "MysteryDyes": lambda x: "Activated effect not yet implemented.",
    "MysteryPortal": lambda x: "Activated effect not yet implemented.",
    "NeonBox": lambda x: "Activated effect not yet implemented.",
    "NewCharSlot": lambda x: "Activated effect not yet implemented.",
    "OPBUFF": lambda x: "Activated effect not yet implemented.",
    "OnraneActivate": lambda x: "Activated effect not yet implemented.",
    "PLootboxActivate": lambda x: "Activated effect not yet implemented.",
    "PartyAOE": lambda x: "Activated effect not yet implemented.",
    "PearlAbility": lambda x: "Activated effect not yet implemented.",
    "PermaPet": lambda x: "Activated effect not yet implemented.",
    "Pet": lambda x: "Activated effect not yet implemented.",
    "PetSkin": lambda x: "Activated effect not yet implemented.",
    "PetStoneActivate": lambda x: "Activated effect not yet implemented.",
    "PoZPage": lambda x: "Activated effect not yet implemented.",
    "PoisonGrenade": lambda x: "Activated effect not yet implemented.",
    "PowerStat": lambda x: "Activated effect not yet implemented.",
    "RageReapBox": lambda x: "Activated effect not yet implemented.",
    "RandomCurrency": lambda x: "Activated effect not yet implemented.",
    "RandomGold": lambda x: "Activated effect not yet implemented.",
    "RandomKantos": lambda x: "Activated effect not yet implemented.",
    "RandomOnrane": lambda x: "Activated effect not yet implemented.",
    "RemoveNegativeConditions": lambda x: "Activated effect not yet implemented.",
    "RemoveNegativeConditionsSelf": lambda x: "Activated effect not yet implemented.",
    "RenamePet": lambda x: "Activated effect not yet implemented.",
    "RevivementBox": lambda x: "Activated effect not yet implemented.",
    "RoyalTrap": lambda x: "Activated effect not yet implemented.",
    "SacredActivate": lambda x: "Activated effect not yet implemented.",
    "SamuraiAbility": lambda x: "Activated effect not yet implemented.",
    "Shoot": lambda x: "Activated effect not yet implemented.",
    "ShootEff": lambda x: "Unused Activated Effect \"ShootEff\".",
    "ShurikenAbility": lambda x: "Activated effect not yet implemented.",
    "SilentBox": lambda x: "Unused Activated Effect \"SilentBox\".",
    "SiphonAbility": lambda x: "Activated effect not yet implemented.",
    "SorConstruct": lambda x: "Constructs a Sor Crystal.",
    "SorForge": lambda x: "Ascends this item to a Legendary Sor Crystal.",
    "SorMachine": lambda x: "Transforms a Legendary Sor Crystal into a useful item.",
    "SpecialPet": lambda x: "Unused Activated Effect \"SpecialPet\".",
    "SpiderTrap": lambda x: "Activated effect not yet implemented.",
    "StasisBlast": lambda x: "Effect on enemies: Within 3 tiles, Stasis for {} seconds. Centered around the player's cursor.".format(x["duration"]),
    "StatBoostAura": lambda x: "Effect on party: Within {} tiles, {:+d} {} for {} seconds. {}".format(x["range"], int(x["amount"]), statName(x["stat"]), x["duration"], wisMod(x)),
    "StatBoostSelf": lambda x: "Effect on self: {:+d} {} for {} seconds. {}".format(int(x["amount"]), statName(x["stat"]), x["duration"], wisMod(x)),
    "Summon": lambda x: "Unused Activated Effect \"Summon\".",
    "SunshineBox": lambda x: "Unused Activated Effect \"SunshineBox\".",
    "TalismanAbility": lambda x: "Activated effect not yet implemented.",
    "Teleport": lambda x: "Teleports the player to the cursor, with a maximum distance of {}.".format(x["maxDistance"]),
    "TomeDamage": lambda x: "Unused Activated Effect \"TomeDamage\".",
    "Torii": lambda x: "Activated effect not yet implemented.",
    "Totem": lambda x: "Unused Activated Effect \"Totem\".",
    "Trap": lambda x: "Activated effect not yet implemented.",
    "TreasureActivate": lambda x: "Grants the player {} gold.".format(x["amount"]),
    "URandomOnrane": lambda x: "Grants the player 12, 14, 16, 18, or 20 onrane.",
    "UnScroll": lambda x: "Unused Activated Effect \"UnScroll\".",
    "Unlock": lambda x: "Unused Activated Effect \"Unlock\".",
    "UnlockEmote": lambda x: "Unlocks the {} emote.".format(x["id"]),
    "UnlockPortal": lambda x: "Unlocks a {}.".format(x["lockedName"]),
    "UnlockSkin": lambda x: "Unlocks skin type {}.".format(x["skinType"]),
    "VampireBlast": lambda x: "Steals {} HP within {} tiles. Centered around the player's cursor.".format(x["totalDamage"], x["radius"]),
    "VorvBox": lambda x: "Unused Activated Effect \"VorvBox\".",
    "WARPAWNBUFF": lambda x: "Unused Activated Effect \"WARPAWNBUFF\".",
    "WigWeekBox": lambda x: "Unused Activated Effect \"WigWeekBox\".",
    "WorldBossActivate": lambda x: "WorldBossActivate not yet implemented.",
    "XPBoost": lambda x: "Grants a 50% loot boost for {} minutes.".format(int(x["duration"]) / 60)
}

# Always capitalize the sentence and put punctuation at the end.
aoeformatter = {
    "IncrementStat": lambda x: "{:+d} {}".format(int(x["amount"]), statName(x["stat"])),
    #only one activateonequip, kinda boring
}