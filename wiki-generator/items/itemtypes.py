

# todo: this file needs to be renamed. slots and stats and activated effects aren't item types.

SacredIDToDesc = {
    0: "Runic Offense: On hit, 8% chance to trigger an AOE damage for 1.5x of taken damage with a 4 tile radius. Stackable.",
    1: "Runic Defense: On hit, 8% chance to trigger an AOE heal for the taken damage with a 4 tile radius. Stackable.",
    2: "Enhanced Growth: Health regeneration is increased by 10% and maximum health is increased by 5%. Stackable.",
    3: "Open Mind: Mana regeneration is increased by 10% and maximum mana is increased by 5%. Stackable.",
    4: "Treasure Hunter: On loot roll, 8% chance to apply a 100% drop chance increase. Stackable.",
    5: "Adrenaline Rush: On hit, 8% chance to ignore incoming damage. Stackable.",
    6: "Arcane Grace: On ability use, 7% chance to not use any mana. Stackable.",
    7: "Helping Hand: On ability use, 7% chance to give 10 attack and 10 defense to each player in a 3 tile radius for 5 seconds. Stackable.",
    8: "Galactic Valor: All status effect durations are increased by 5%. Stackable.",
    9: "Collector's Edition: All stats are increased by 0.65% per sacred item in inventory. Stackable.",
    10: "Critical Focus: On enemy hit, 7% chance to increase might by 10% of total luck. Stackable."
}

SlotToCategory = {
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

SlotToSlotType = {
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

StatIDToName = {
    0: "Maximum HP",
    2: "Size",
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
    "2": "Size",
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

def formatRandVals(ae):
    randVals = ae["randVals"]
    effs = randVals.replace(" ", "").split(",")
    if (len(effs) == 0):
        return "Sick or Bravery"
    elif (len(effs) == 1):
        return effs[0]
    elif (len(effs) == 2):
        return " or ".join(effs)
    else:
        ret = ", ".join(effs[:-1])
        ret += ", or " + effs[-1]
        return ret

def pluralize(ae, attr, text):
    att = ae[attr]
    ret = att + " " + text
    if (abs(float(att) - 1.0) < 0.001):
        return ret
    else:
        return ret + "s"

def pMinutes(ae):
    att = round(int(ae["duration"]) / 60, 2) # duration is in seconds
    if (abs(att - 1.0) < 0.001):
        return str(att) + " minute"
    else:
        return str(att) + " minutes"

pRange = lambda x: pluralize(x, "range", "tile")
pDuration = lambda x: pluralize(x, "duration", "second")

statName = lambda x: StatIDToName.get(x, "unknown stat")
wismod = lambda x: " Uses wis mod." if x.get("useWisMod", "") == "true" else " Does not use wis mod."
unusedAE = lambda eff: "Unused Activated Effect: " + eff + "."
notImplementedAE = lambda eff: "\"" + eff + "\" Activated Effect not implemented."
emptyAE = ""



# Always capitalize the sentence and put punctuation at the end.
AOEFormatter = {
    "IncrementStat": lambda x: "{:+d} {}.".format(int(x["amount"]), statName(x["stat"])),
    "EffectEquip": lambda x: "Grants {} after {}.".format(x["effect"], pluralize(x, "delay", "second"))
}

# Alays capitalize the sentence and put punctuation at the end.
AEFormatter = {
    # unused activated effects
    "AbbyConstruct": lambda x: unusedAE("AbbyConstruct"),
    "AnguishofDrannol": lambda x: unusedAE("AnguishofDrannol"),
    "AsiimovBox": lambda x: unusedAE("AsiimovBox"),
    "Belt": lambda x: unusedAE("Belt"),
    "BigStasisBlast": lambda x: unusedAE("BigStasisBlast"),
    "BlizzardBox": lambda x: unusedAE("BlizzardBox"),
    "BronzeLockbox": lambda x: unusedAE("BronzeLockbox"),
    "BulletNova2": lambda x: unusedAE("BulletNova2"),
    "BurningLightning": lambda x: unusedAE("BurningLightning"),
    "ChangeSkin": lambda x: unusedAE("ChangeSkin"),
    "ChristmasPopper": lambda x: unusedAE("ChristmasPopper"),
    "CrimsonBox": lambda x: unusedAE("CrimsonBox"),
    "DareFistBox": lambda x: unusedAE("DareFistBox"),
    "DazeBlast": lambda x: unusedAE("DazeBlast"),
    "Drake": lambda x: unusedAE("Drake"),
    "DualShoot": lambda x: unusedAE("DualShoot"),
    "Fame": lambda x: unusedAE("Fame"),
    "FixedStat": lambda x: unusedAE("FixedStat"),
    "GPBox": lambda x: unusedAE("GPBox"),
    "Halo": lambda x: unusedAE("Halo"),
    "HealingGrenade": lambda x: unusedAE("HealingGrenade"),
    "HeldEffect": lambda x: unusedAE("HeldEffect"),
    "IdScroll": lambda x: unusedAE("IdScroll"),
    "MayhemBox": lambda x: unusedAE("MayhemBox"),
    "MiniPot": lambda x: unusedAE("MiniPot"),
    "MonsterToss": lambda x: unusedAE("MonsterToss"),
    "MultiDecoy": lambda x: unusedAE("MultiDecoy"),
    "Mushroom": lambda x: unusedAE("Mushroom"),
    "MysteryDyes": lambda x: unusedAE("MysteryDyes"),
    "NeonBox": lambda x: unusedAE("NeonBox"),
    "NewCharSlot": lambda x: unusedAE("NewCharSlot"),
    "PLootboxActivate": lambda x: unusedAE("PLootboxActivate"),
    "PartyAOE": lambda x: unusedAE("PartyAOE"),
    "PearlAbility": lambda x: unusedAE("PearlAbility"),
    "PetSkin": lambda x: unusedAE("PetSkin"),
    "PoZPage": lambda x: unusedAE("PoZPage"),
    "RageReapBox": lambda x: unusedAE("RageReapBox"),
    "RandomKantos": lambda x: unusedAE("RandomKantos"),
    "RDiceActivate": lambda x: unusedAE("RDiceActivate"),
    "RenamePet": lambda x: unusedAE("RenamePet"),
    "RevivementBox": lambda x: unusedAE("RevivementBox"),
    "ShootEff": lambda x: unusedAE("ShootEff"),
    "SilentBox": lambda x: unusedAE("SilentBox"),
    "SpecialPet": lambda x: unusedAE("SpecialPet"),
    "Summon": lambda x: unusedAE("Summon"),
    "SunshineBox": lambda x: unusedAE("SunshineBox"),
    "TomeDamage": lambda x: unusedAE("TomeDamage"),
    "Totem": lambda x: unusedAE("Totem"),
    "UnScroll": lambda x: unusedAE("UnScroll"),
    "Unlock": lambda x: unusedAE("Unlock"),
    "VorvBox": lambda x: unusedAE("VorvBox"),
    "WARPAWNBUFF": lambda x: unusedAE("WARPAWNBUFF"),
    "WigWeekBox": lambda x: unusedAE("WigWeekBox"),
    "WorldBossActivate": lambda x: unusedAE("WorldBossActivate"),

    # used on some items but don't do anything
    "AsiHeal": lambda x: notImplementedAE("AsiHeal"),
    "BlackScroll": lambda x: notImplementedAE("BlackScroll"),
    "BrownScroll": lambda x: notImplementedAE("BuildTower"),
    "BuildTower": lambda x: notImplementedAE("BuildTower"),
    "ClearConditionEffectSelf": lambda x: notImplementedAE("ClearConditionEffectSelf"),
    "CreateGauntlet": lambda x: notImplementedAE("CreateGauntlet"),
    "CreatePet": lambda x: notImplementedAE("CreatePet"),
    "Dice": lambda x: notImplementedAE("Dice"),
    "FUnlockPortal": lambda x: notImplementedAE("FUnlockPortal"),
    "HealNovaSigil": lambda x: notImplementedAE("HealNovaSigil"),
    "LootboxActivate": lambda x: notImplementedAE("LootboxActivate"),
    "MysteryPortal": lambda x: notImplementedAE("MysteryPortal"),
    "OPBUFF": lambda x: notImplementedAE("OPBUFF"),
    "PermaPet": lambda x: notImplementedAE("PermaPet"),
    "PetStoneActivate": lambda x: notImplementedAE("PetStoneActivate"),
    "RoyalTrap": lambda x: notImplementedAE("RoyalTrap"),
    "SpiderTrap": lambda x: notImplementedAE("SpiderTrap"),

    # tooltips that are made by <ExtraTooltipInfo> or something
    "AscensionActivate": lambda x: emptyAE,
    "AstonAbility": lambda x: emptyAE, # does the same as Shoot
    "BurstInferno": lambda x: emptyAE,
    "DreamEssenceActivate": lambda x: emptyAE,
    "FameActivate": lambda x: emptyAE,
    "Gift": lambda x: emptyAE,
    "InsigniaActivate": lambda x: emptyAE,
    "JacketAbility": lambda x: emptyAE,
    "JacketAbility2": lambda x: emptyAE,
    "MarksActivate": lambda x: emptyAE,
    "SamuraiAbility": lambda x: emptyAE,
    "Shoot": lambda x: emptyAE,
    "ShurikenAbility": lambda x: emptyAE,
    "SiphonAbility": lambda x: emptyAE,
    "TalismanAbility": lambda x: emptyAE,

    "ActivateFragment": lambda x:
        "Grants the player either 5, 10, or 15 Sacred Fragments.",

    "Backpack": lambda x:
        "Unlocks the player's backpack.",

    "Banner": lambda x:
        "Within {}, empowers allies for {}. Stays active for {}."
        .format(pRange(x), pDuration(x), pluralize(x, "amount", "second")),

    "BulletNova": lambda x:
        "Shoots 12 shots in a circle around the cursor.",

    "ClearConditionEffectAura": lambda x:
        "Within {}: if a player has the effect {}, removes {} from them."
        .format(pRange(x), x["checkExistingEffect"], x["effect"]),

    "ConditionEffectAura": lambda x:
        "Party effect: {} for {} within {}.{}"
        .format(x["effect"], pDuration(x), pRange(x), wismod(x)),

    "ConditionEffectSelf": lambda x:
        "On self: {} for {}.{}"
        .format(x["effect"], pDuration(x), wismod(x)),

    "Create": lambda x:
        "Creates a {}."
        .format(x["id"]),

    "DDiceActivate": lambda x:
        "Grants Weak, Bravery, or Damaging for {}."
        .format(pDuration(x)),

    "DamageNova": lambda x:
        "Does {} damage within {}.{}"
        .format(x["amount"], pRange(x), wismod(x)),

    "Decoy": lambda x:
        "Creates a decoy that lasts for {}."
        .format(pDuration(x)),

    "DiceActivate": lambda x:
        "Grants {} for {}."
        .format(formatRandVals(x), pDuration(x)),

    "Dye": lambda x:
        "Changes the character's dye.",

    "EffectRandom": lambda x:
        "Grants a random effect.",

    "GenericActivate": lambda x:
        "{} Effect: "
        .format("Enemy" if x["target"] == "enemy" else "Party")
        + "{} for {} within {}. "
        .format(x["effect"], pDuration(x), pRange(x))
        + "Centered around the {}."
        .format("player's cursor" if x["center"] == "mouse" else x["center"]),

    "Heal": lambda x:
        "Heals {} health."
        .format(x["amount"]),

    "Heal2": lambda x:
        "Heals health based on the player's Restoration stat.",

    "HealNova": lambda x:
        "Heals {} HP within {}.{}"
        .format(x["amount"], pRange(x), wismod(x)),

    "IncrementStat": lambda x:
        "Permanently increases {} by {}."
        .format(statName(x["stat"]), x["amount"]),

    "LDBoost": lambda x:
        "Increases loot drop chance by 50% for {}."
        .format(pMinutes(x)),

    "LTBoost": lambda x:
        "Increases loot tier by 1 for {}."
        .format(pMinutes(x)),

    "Lightning": lambda x:
        "Lightning: {} damage to {}.{}"
        .format(x["totalDamage"], pluralize(x, "maxTargets", "target"), wismod(x))
        + ("\nLightning effect: {} for {}."
            .format(x["condEffect"], pluralize(x, "condDuration", "second"))
            if x.get("condEffect", "") != "" else ""),

    "Magic": lambda x:
        "Restores {} mana."
        .format(x["amount"]),

    "Magic2": lambda x:
        "Restores mana based on the player's restoration.",

    "MagicNova": lambda x:
        "Restores {} mana within {}."
        .format(x["amount"], pRange(x)),

    "OnraneActivate": lambda x:
        "Grants the player {} onrane."
        .format(x["amount"]),

    "Pet": lambda x:
        "Creates a {} pet."
        .format(x["objectId"]),

    "PoisonGrenade": lambda x:
        "Poison Grenade:\n"
        + "After {}, {} impact damage + {} damage over {}.{}"
        .format(pluralize(x, "throwTime", "second"), x["impactDamage"], x["totalDamage"], pDuration(x), wismod(x)),

    "PowerStat": lambda x:
        "Permanently increases {} by {}. Can only be used by ascended characters."
        .format(StatIDToName[x["stat"]], x["amount"]),

    "RandomCurrency": lambda x:
        "Grants the player either {} {}."
        .format(formatRandVals(x), x["currencyType"]),

    "RandomGold": lambda x:
        "Grants the player either 250, 500, or 750 gold.",

    "RandomOnrane": lambda x:
        "Grants the player either 2, 4, 6, 8, or 10 onrane.",

    "RemoveNegativeConditions": lambda x:
        "Removes negative conditions from players within {}."
        .format(pRange(x)),

    "RemoveNegativeConditionsSelf": lambda x:
        "Removes negative condition effects from self.",

    "SacredActivate": lambda x:
        "Grants the player {}."
        .format(pluralize(x, "amount", "sacred fragment")),

    "SorConstruct": lambda x:
        "Constructs a Sor Crystal.",

    "SorForge": lambda x:
        "This item can be ascended into a Legendary Sor Crystal.",

    "SorMachine": lambda x:
        "Transforms a Legendary Sor Crystal into a useful item.",

    "StasisBlast": lambda x:
        "Enemy effect: Within 3 tiles of the player's cursor, Stasis for {}."
        .format(pDuration(x)),

    "StatBoostAura": lambda x:
        "Party effect: Within {}, {:+d} {} for {}.{}"
        .format(pRange(x), int(x["amount"]), statName(x["stat"]), pDuration(x), wismod(x)),

    "StatBoostSelf": lambda x:
        "Effect on self: {:+d} {} for {}.{}"
        .format(int(x["amount"]), statName(x["stat"]), pDuration(x), wismod(x)),

    "Teleport": lambda x:
        "Teleports the player to the cursor, with a maximum distance of {}."
        .format(pluralize(x, "maxDistance", "tile")),

    "Torii": lambda x:
        "Spawns {} Torii.\n"
        .format("a defensive" if x["players"] == "true" else "an offensive")
        + "Within {}: {} for {}.\n"
        .format(pRange(x), x["effect"], pDuration(x))
        + "Disappears after {}."
        .format(pluralize(x, "amount", "second")),

    "Trap": lambda x:
        "Trap: {} damage within {}."
        .format(x["totalDamage"], pluralize(x, "radius", "tile"))
        + ("\nOn enemies: {} for {}."
            .format(x["condEffect"], pluralize(x, "condDuration", "second"))
            if x.get("condEffect", "") != "" else "")
        + ("\nThrow time: {}."
            .format(pluralize(x, "throwTime", "second"))
            if x.get("throwTime", "") != "" else "\nThrow time: 1 second."),

    "TreasureActivate": lambda x:
        "Grants the player {} gold."
        .format(x["amount"]),

    "URandomOnrane": lambda x:
        "Grants the player 12, 14, 16, 18, or 20 onrane.",

    "UnlockEmote": lambda x:
        "Unlocks the {} emote."
        .format(x["id"]),

    "UnlockPortal": lambda x:
        "Unlocks a{} {}."
        .format("n" if x["lockedName"][0] in "AEIOUaeiou" else "", x["lockedName"]),

    "UnlockSkin": lambda x:
        "Unlocks skin type {}."
        .format(x["skinType"]),

    "VampireBlast": lambda x:
        "Steals {} HP within {}. Centered around the player's cursor."
        .format(x["totalDamage"], pluralize(x, "radius", "tile")),

    "XPBoost": lambda x:
        "Grants a 50% experience boost for {}."
        .format(pMinutes(x))
}
