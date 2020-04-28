from xmltags import SetElementData

class Item():

    Item = True
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
            ret = this.Id + "\n"
            ret += "Object Type " + hex(this.ObjType) + "\n"
            ret += this.Description + "\n" if this.Description else ""
            if (this.ActivateOnEquip):
                ret += "\nWhile equipped:\n"
                aes = []
                for ae in this.ActivateOnEquip:
                    aes.append(aoeformatter.get(ae[0], lambda x: "Unknown AE \"" + ae[0] + "\" on item \"" + this.Id + "\"")(ae[1]))
                aes.sort()
                ret += "\n".join(aes) + "\n"

            if (this.Activate):
                ret += "\nWhen used:\n"
                aes = []
                for ae in this.Activate:
                    aes.append(aeformatter.get(ae[0], lambda x: "Unknown AE \"" + ae[0] + "\" on item \"" + this.Id + "\"")(ae[1]))
                aes.sort()
                ret += "\n".join(aes) + "\n"
            return ret
        except:
            return "Error when converting \"" + this.Id + "\" to string.\n"

    def set(this, variableName, value):
        setattr(this, str(variableName), value)

    def get(this, variableName):
        return getattr(this, variableName)












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
    "AbbyConstruct": lambda x: "\"AbbyConstruct\" Activated Effect not yet implemented.",
    "ActivateFragment": lambda x: "\"ActivateFragment\" Activated Effect not yet implemented.",
    "AnguishofDrannol": lambda x: "\"AnguishofDrannol\" Activated Effect not yet implemented.",
    "AscensionActivate": lambda x: "\"AscensionActivate\" Activated Effect not yet implemented.",
    "AsiHeal": lambda x: "\"AsiHeal\" Activated Effect not yet implemented.",
    "AsiimovBox": lambda x: "\"AsiimovBox\" Activated Effect not yet implemented.",
    "AstonAbility": lambda x: "\"AstonAbility\" Activated Effect not yet implemented.",
    "Backpack": lambda x: "\"Backpack\" Activated Effect not yet implemented.",
    "Banner": lambda x: "\"Banner\" Activated Effect not yet implemented.",
    "Belt": lambda x: "\"Belt\" Activated Effect not yet implemented.",
    "BigStasisBlast": lambda x: "\"BigStasisBlast\" Activated Effect not yet implemented.",
    "BlackScroll": lambda x: "\"BlackScroll\" Activated Effect not yet implemented.",
    "BlizzardBox": lambda x: "\"BlizzardBox\" Activated Effect not yet implemented.",
    "BronzeLockbox": lambda x: "\"BronzeLockbox\" Activated Effect not yet implemented.",
    "BrownScroll": lambda x: "\"BrownScroll\" Activated Effect not yet implemented.",
    "BuildTower": lambda x: "\"BuildTower\" Activated Effect not yet implemented.",
    "BulletNova": lambda x: "\"BulletNova\" Activated Effect not yet implemented.",
    "BulletNova2": lambda x: "\"BulletNova2\" Activated Effect not yet implemented.",
    "BurningLightning": lambda x: "\"BurningLightning\" Activated Effect not yet implemented.",
    "BurstInferno": lambda x: "\"BurstInferno\" Activated Effect not yet implemented.",
    "ChangeSkin": lambda x: "\"ChangeSkin\" Activated Effect not yet implemented.",
    "ChristmasPopper": lambda x: "\"ChristmasPopper\" Activated Effect not yet implemented.",
    "ClearConditionEffectAura": lambda x: "\"ClearConditionEffectAura\" Activated Effect not yet implemented.",
    "ClearConditionEffectSelf": lambda x: "\"ClearConditionEffectSelf\" Activated Effect not yet implemented.",
    "ConditionEffectAura": lambda x: "\"ConditionEffectAura\" Activated Effect not yet implemented.",
    "ConditionEffectSelf": lambda x: "\"ConditionEffectSelf\" Activated Effect not yet implemented.",
    "Create": lambda x: "\"Create\" Activated Effect not yet implemented.",
    "CreateGauntlet": lambda x: "\"CreateGauntlet\" Activated Effect not yet implemented.",
    "CreatePet": lambda x: "\"CreatePet\" Activated Effect not yet implemented.",
    "CrimsonBox": lambda x: "\"CrimsonBox\" Activated Effect not yet implemented.",
    "DDiceActivate": lambda x: "\"DDiceActivate\" Activated Effect not yet implemented.",
    "DamageNova": lambda x: "\"DamageNova\" Activated Effect not yet implemented.",
    "DareFistBox": lambda x: "\"DareFistBox\" Activated Effect not yet implemented.",
    "DazeBlast": lambda x: "\"DazeBlast\" Activated Effect not yet implemented.",
    "Decoy": lambda x: "\"Decoy\" Activated Effect not yet implemented.",
    "Dice": lambda x: "\"Dice\" Activated Effect not yet implemented.",
    "DiceActivate": lambda x: "\"DiceActivate\" Activated Effect not yet implemented.",
    "Drake": lambda x: "\"Drake\" Activated Effect not yet implemented.",
    "DreamEssenceActivate": lambda x: "\"DreamEssenceActivate\" Activated Effect not yet implemented.",
    "DualShoot": lambda x: "\"DualShoot\" Activated Effect not yet implemented.",
    "Dye": lambda x: "\"Dye\" Activated Effect not yet implemented.",
    "EffectRandom": lambda x: "\"EffectRandom\" Activated Effect not yet implemented.",
    "FUnlockPortal": lambda x: "Unlocks a {}.".format(x["lockedName"]),
    "Fame": lambda x: "\"Fame\" Activated Effect not yet implemented.",
    "FameActivate": lambda x: "\"FameActivate\" Activated Effect not yet implemented.",
    "FixedStat": lambda x: "\"FixedStat\" Activated Effect not yet implemented.",
    "GPBox": lambda x: "\"GPBox\" Activated Effect not yet implemented.",
    "GenericActivate": lambda x: "\"GenericActivate\" Activated Effect not yet implemented.",
    "Gift": lambda x: "\"Gift\" Activated Effect not yet implemented.",
    "Halo": lambda x: "\"Halo\" Activated Effect not yet implemented.",
    "Heal": lambda x: "\"Heal\" Activated Effect not yet implemented.",
    "Heal2": lambda x: "\"Heal2\" Activated Effect not yet implemented.",
    "HealNova": lambda x: "Heals {} HP within {} tiles. {}".format(x["amount"], float(x["range"]), wisMod(x)),
    "HealNovaSigil": lambda x: "\"HealNovaSigil\" Activated Effect not yet implemented.",
    "HealingGrenade": lambda x: "\"HealingGrenade\" Activated Effect not yet implemented.",
    "HeldEffect": lambda x: "\"HeldEffect\" Activated Effect not yet implemented.",
    "IdScroll": lambda x: "\"IdScroll\" Activated Effect not yet implemented.",
    "IncrementStat": lambda x: "Permanently increases {} by {}.".format(statName(x["stat"]), x["amount"]),
    "InsigniaActivate": lambda x: "\"InsigniaActivate\" Activated Effect not yet implemented.",
    "JacketAbility": lambda x: "\"JacketAbility\" Activated Effect not yet implemented.",
    "JacketAbility2": lambda x: "\"JacketAbility2\" Activated Effect not yet implemented.",
    "LDBoost": lambda x: "\"LDBoost\" Activated Effect not yet implemented.",
    "LTBoost": lambda x: "\"LTBoost\" Activated Effect not yet implemented.",
    "Lightning": lambda x: "\"Lightning\" Activated Effect not yet implemented.",
    "LootboxActivate": lambda x: "\"LootboxActivate\" Activated Effect not yet implemented.",
    "Magic": lambda x: "\"Magic\" Activated Effect not yet implemented.",
    "Magic2": lambda x: "\"Magic2\" Activated Effect not yet implemented.",
    "MagicNova": lambda x: "\"MagicNova\" Activated Effect not yet implemented.",
    "MarksActvate": lambda x: "\"MarksActivate\" Activated Effect not yet implemented.",
    "MayhemBox": lambda x: "\"MayhemBox\" Activated Effect not yet implemented.",
    "MiniPot": lambda x: "\"MiniPot\" Activated Effect not yet implemented.",
    "MonsterToss": lambda x: "\"MonsterToss\" Activated Effect not yet implemented.",
    "MultiDecoy": lambda x: "\"MultiDecoy\" Activated Effect not yet implemented.",
    "Mushroom": lambda x: "\"Mushroom\" Activated Effect not yet implemented.",
    "MysteryDyes": lambda x: "\"MysteryDyes\" Activated Effect not yet implemented.",
    "MysteryPortal": lambda x: "\"MysteryPortal\" Activated Effect not yet implemented.",
    "NeonBox": lambda x: "\"NeonBox\" Activated Effect not yet implemented.",
    "NewCharSlot": lambda x: "\"NewCharSlot\" Activated Effect not yet implemented.",
    "OPBUFF": lambda x: "\"OPBUFF\" Activated Effect not yet implemented.",
    "OnraneActivate": lambda x: "\"OnraneActivate\" Activated Effect not yet implemented.",
    "PLootboxActivate": lambda x: "\"PLootboxActivate\" Activated Effect not yet implemented.",
    "PartyAOE": lambda x: "\"PartyAOE\" Activated Effect not yet implemented.",
    "PearlAbility": lambda x: "\"PearlAbility\" Activated Effect not yet implemented.",
    "PermaPet": lambda x: "\"PermaPet\" Activated Effect not yet implemented.",
    "Pet": lambda x: "\"Pet\" Activated Effect not yet implemented.",
    "PetSkin": lambda x: "\"PetSkin\" Activated Effect not yet implemented.",
    "PetStoneActivate": lambda x: "\"PetStoneActivate\" Activated Effect not yet implemented.",
    "PoZPage": lambda x: "\"PoZPage\" Activated Effect not yet implemented.",
    "PoisonGrenade": lambda x: "\"PoisonGrenade\" Activated Effect not yet implemented.",
    "PowerStat": lambda x: "\"PowerStat\" Activated Effect not yet implemented.",
    "RageReapBox": lambda x: "\"RageReapBox\" Activated Effect not yet implemented.",
    "RandomCurrency": lambda x: "\"RandomCurrency\" Activated Effect not yet implemented.",
    "RandomGold": lambda x: "\"RandomGold\" Activated Effect not yet implemented.",
    "RandomKantos": lambda x: "\"RandomKantos\" Activated Effect not yet implemented.",
    "RandomOnrane": lambda x: "\"RandomOnrane\" Activated Effect not yet implemented.",
    "RemoveNegativeConditions": lambda x: "\"RemoveNegativeConditions\" Activated Effect not yet implemented.",
    "RemoveNegativeConditionsSelf": lambda x: "\"RemoveNegativeConditionsSelf\" Activated Effect not yet implemented.",
    "RenamePet": lambda x: "\"RenamePet\" Activated Effect not yet implemented.",
    "RevivementBox": lambda x: "\"RevivementBox\" Activated Effect not yet implemented.",
    "RoyalTrap": lambda x: "\"RoyalTrap\" Activated Effect not yet implemented.",
    "SacredActivate": lambda x: "\"SacredActivate\" Activated Effect not yet implemented.",
    "SamuraiAbility": lambda x: "\"SamuraiAbility\" Activated Effect not yet implemented.",
    "Shoot": lambda x: "\"Shoot\" Activated Effect not yet implemented.",
    "ShootEff": lambda x: "Unused Activated Effect \"ShootEff\".",
    "ShurikenAbility": lambda x: "\"ShurikenAbility\" Activated Effect not yet implemented.",
    "SilentBox": lambda x: "Unused Activated Effect \"SilentBox\".",
    "SiphonAbility": lambda x: "\"SiphonAbility\" Activated Effect not yet implemented.",

    "SorConstruct": lambda x: "Constructs a Sor Crystal.",
    "SorForge": lambda x: "Ascends this item to a Legendary Sor Crystal.",
    "SorMachine": lambda x: "Transforms a Legendary Sor Crystal into a useful item.",
    "SpecialPet": lambda x: "Unused Activated Effect \"SpecialPet\".",
    "SpiderTrap": lambda x: "\"SpiderTrap\" Activated Effect not yet implemented.",
    "StasisBlast": lambda x: "Effect on enemies: Within 3 tiles, Stasis for {} seconds. Centered around the player's cursor.".format(x["duration"]),
    "StatBoostAura": lambda x: "Effect on party: Within {} tiles, {:+d} {} for {} seconds. {}".format(x["range"], int(x["amount"]), statName(x["stat"]), x["duration"], wisMod(x)),
    "StatBoostSelf": lambda x: "Effect on self: {:+d} {} for {} seconds. {}".format(int(x["amount"]), statName(x["stat"]), x["duration"], wisMod(x)),
    "Summon": lambda x: "Unused Activated Effect \"Summon\".",
    "SunshineBox": lambda x: "Unused Activated Effect \"SunshineBox\".",
    "TalismanAbility": lambda x: "\"TalismanAbility\" Activated Effect not yet implemented.",
    "Teleport": lambda x: "Teleports the player to the cursor, with a maximum distance of {}.".format(x["maxDistance"]),
    "TomeDamage": lambda x: "Unused Activated Effect \"TomeDamage\".",
    "Torii": lambda x: "\"Torii\" Activated Effect not yet implemented.",
    "Totem": lambda x: "Unused Activated Effect \"Totem\".",
    "Trap": lambda x: "\"Trap\" Activated Effect not yet implemented.",
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