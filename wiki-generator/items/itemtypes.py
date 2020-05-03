

# todo: this file needs to be renamed. slots and stats and activated effects aren't item types.

SacredIDToDesc = {
    0: "Runic Offense: On hit, 8% chance to trigger an AOE damage for 1.5x of taken damage with a 4 tile radius. Stackable.",
    1: "Runic Defense: On hit, 8% chance to trigger an AOE heal for the taken damage with a 4 tile radius. Stackable.",
    2: "Enhanced Growth: Health regeneration is increased by 10% and maximum health is increased by 5%. Stackable.",
    3: "Open Mind: Mana regeneration is increased by 10% and maximum mana is increased by 5%. Stackable.",
    4: "Treasure Hunter: On loot roll, 8% chance to apply a 100% drop chance increase. Stackable.",
    5: "Adrenaline Rush: On hit, 8% chance to ignore incoming damage. Stackable.",
    6: "Arcane Grace: On ability use, 7% chance to not use any mana. Stackable.",
    7: "Helping Hand: On ability use, 7% chance to remove 1 negative effect per player in a 3 tile radius. Stackable.",
    8: "Galactic Valor: All status effect durations are increased by 5%. Stackable.",
    9: "Collector's Edition: All stats are increased by 0.75% per sacred item in inventory. Stackable.",
    10: "Critical Focus: On enemy hit, 7% increase might by 10% of total luck. Stackable."
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

statName = lambda x: StatIDToName.get(x, "unknown stat")
wisMod = lambda x: "Uses wis mod." if x.get("useWisMod", "") == "true" else "Does not use wis mod."
unusedAE = lambda eff: "Unused Activated Effect: " + eff + "."
emptyAE = ""



# Always capitalize the sentence and put punctuation at the end.
AOEFormatter = {
    "IncrementStat": lambda x: "{:+d} {}.".format(int(x["amount"]), statName(x["stat"])),
    "EffectEquip": lambda x: "Grants {} after {} seconds.".format(x["effect"], x["delay"])
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


    "SamuraiAbility": lambda x: emptyAE,
    "Shoot": lambda x: emptyAE,
    "ShurikenAbility": lambda x: emptyAE,
    "SiphonAbility": lambda x: emptyAE,


    "ActivateFragment": lambda x:
        "\"ActivateFragment\" Activated Effect not yet implemented.",

    "AscensionActivate": lambda x:
        "\"AscensionActivate\" Activated Effect not yet implemented.",

    "AsiHeal": lambda x:
        "\"AsiHeal\" Activated Effect not yet implemented.",

    "AstonAbility": lambda x:
        "\"AstonAbility\" Activated Effect not yet implemented.",

    "Backpack": lambda x:
        "\"Backpack\" Activated Effect not yet implemented.",

    "Banner": lambda x:
        "\"Banner\" Activated Effect not yet implemented.",

    "BlackScroll": lambda x:
        "\"BlackScroll\" Activated Effect not yet implemented.",

    "BrownScroll": lambda x:
        "\"BrownScroll\" Activated Effect not yet implemented.",

    "BuildTower": lambda x:
        "\"BuildTower\" Activated Effect not yet implemented.",

    "BulletNova": lambda x:
        "\"BulletNova\" Activated Effect not yet implemented.",

    "BulletNova2": lambda x:
        "\"BulletNova2\" Activated Effect not yet implemented.",

    "BurstInferno": lambda x:
        "\"BurstInferno\" Activated Effect not yet implemented.",

    "ClearConditionEffectAura": lambda x:
        "\"ClearConditionEffectAura\" Activated Effect not yet implemented.",

    "ClearConditionEffectSelf": lambda x:
        "\"ClearConditionEffectSelf\" Activated Effect not yet implemented.",

    "ConditionEffectAura": lambda x:
        "\"ConditionEffectAura\" Activated Effect not yet implemented.",

    "ConditionEffectSelf": lambda x:
        "\"ConditionEffectSelf\" Activated Effect not yet implemented.",

    "Create": lambda x:
        "\"Create\" Activated Effect not yet implemented.",

    "CreateGauntlet": lambda x:
        "\"CreateGauntlet\" Activated Effect not yet implemented.",

    "CreatePet": lambda x:
        "\"CreatePet\" Activated Effect not yet implemented.",

    "DDiceActivate": lambda x:
        "\"DDiceActivate\" Activated Effect not yet implemented.",

    "DamageNova": lambda x:
        "\"DamageNova\" Activated Effect not yet implemented.",

    "Decoy": lambda x:
        "\"Decoy\" Activated Effect not yet implemented.",

    "Dice": lambda x:
        "\"Dice\" Activated Effect not yet implemented.",

    "DiceActivate": lambda x:
        "\"DiceActivate\" Activated Effect not yet implemented.",

    "DreamEssenceActivate": lambda x:
        "\"DreamEssenceActivate\" Activated Effect not yet implemented.",

    "Dye": lambda x:
        "\"Dye\" Activated Effect not yet implemented.",

    "EffectRandom": lambda x:
        "\"EffectRandom\" Activated Effect not yet implemented.",

    "FUnlockPortal": lambda x:
        "Unlocks a {}.".format(x["lockedName"]),

    "FameActivate": lambda x:
        "\"FameActivate\" Activated Effect not yet implemented.",

    "GenericActivate": lambda x:
        "\"GenericActivate\" Activated Effect not yet implemented.",

    "Gift": lambda x:
        "\"Gift\" Activated Effect not yet implemented.",

    "Heal": lambda x:
        "\"Heal\" Activated Effect not yet implemented.",

    "Heal2": lambda x:
        "\"Heal2\" Activated Effect not yet implemented.",

    "HealNova": lambda x:
        "Heals {} HP within {} tiles. {}"
        .format(x["amount"], float(x["range"]), wisMod(x)),

    "HealNovaSigil": lambda x:
        "\"HealNovaSigil\" Activated Effect not yet implemented.",

    "IncrementStat": lambda x:
        "Permanently increases {} by {}."
        .format(statName(x["stat"]), x["amount"]),

    "InsigniaActivate": lambda x:
        "\"InsigniaActivate\" Activated Effect not yet implemented.",

    "JacketAbility": lambda x:
        "\"JacketAbility\" Activated Effect not yet implemented.",

    "JacketAbility2": lambda x:
        "\"JacketAbility2\" Activated Effect not yet implemented.",

    "LDBoost": lambda x:
        "\"LDBoost\" Activated Effect not yet implemented.",

    "LTBoost": lambda x:
        "\"LTBoost\" Activated Effect not yet implemented.",

    "Lightning": lambda x:
        "\"Lightning\" Activated Effect not yet implemented.",

    "LootboxActivate": lambda x:
        "\"LootboxActivate\" Activated Effect not yet implemented.",

    "Magic": lambda x:
        "\"Magic\" Activated Effect not yet implemented.",

    "Magic2": lambda x:
        "\"Magic2\" Activated Effect not yet implemented.",

    "MagicNova": lambda x:
        "\"MagicNova\" Activated Effect not yet implemented.",

    "MarksActivate": lambda x:
        "\"MarksActivate\" Activated Effect not yet implemented.",

    "MysteryPortal": lambda x:
        "\"MysteryPortal\" Activated Effect not yet implemented.",

    "OPBUFF": lambda x:
        "\"OPBUFF\" Activated Effect not yet implemented.",

    "OnraneActivate": lambda x:
        "\"OnraneActivate\" Activated Effect not yet implemented.",

    "PermaPet": lambda x:
        "\"PermaPet\" Activated Effect not yet implemented.",

    "Pet": lambda x:
        "\"Pet\" Activated Effect not yet implemented.",

    "PetStoneActivate": lambda x:
        "\"PetStoneActivate\" Activated Effect not yet implemented.",

    "PoisonGrenade": lambda x:
        "\"PoisonGrenade\" Activated Effect not yet implemented.",

    "PowerStat": lambda x:
        "\"PowerStat\" Activated Effect not yet implemented.",

    "RandomCurrency": lambda x:
        "\"RandomCurrency\" Activated Effect not yet implemented.",

    "RandomGold": lambda x:
        "\"RandomGold\" Activated Effect not yet implemented.",

    "RandomOnrane": lambda x:
        "\"RandomOnrane\" Activated Effect not yet implemented.",

    "RemoveNegativeConditions": lambda x:
        "\"RemoveNegativeConditions\" Activated Effect not yet implemented.",

    "RemoveNegativeConditionsSelf": lambda x:
        "\"RemoveNegativeConditionsSelf\" Activated Effect not yet implemented.",

    "RoyalTrap": lambda x:
        "\"RoyalTrap\" Activated Effect not yet implemented.",

    "SacredActivate": lambda x:
        "Grants the player {} sacred fragments."
        .format(x["amount"]),

    "SorConstruct": lambda x:
        "Constructs a Sor Crystal.",

    "SorForge": lambda x:
        "This item can be ascended into a Legendary Sor Crystal.",

    "SorMachine": lambda x:
        "Transforms a Legendary Sor Crystal into a useful item.",

    "SpiderTrap": lambda x:
        "\"SpiderTrap\" Activated Effect not yet implemented.",

    "StasisBlast": lambda x:
        "Effect on enemies: Within 3 tiles of the player's cursor, Stasis for {} seconds."
        .format(x["duration"]),

    "StatBoostAura": lambda x:
        "Effect on party: Within {} tiles, {:+d} {} for {} seconds. {}"
        .format(x["range"], int(x["amount"]), statName(x["stat"]), x["duration"], wisMod(x)),

    "StatBoostSelf": lambda x:
        "Effect on self: {:+d} {} for {} seconds. {}"
        .format(int(x["amount"]), statName(x["stat"]), x["duration"], wisMod(x)),

    "TalismanAbility": lambda x:
        "\"TalismanAbility\" Activated Effect not yet implemented.",

    "Teleport": lambda x:
        "Teleports the player to the cursor, with a maximum distance of {} tiles."
        .format(x["maxDistance"]),

    "Torii": lambda x:
        "\"Torii\" Activated Effect not yet implemented.",

    "Trap": lambda x:
        "\"Trap\" Activated Effect not yet implemented.",

    "TreasureActivate": lambda x:
        "Grants the player {} gold."
        .format(x["amount"]),

    "URandomOnrane": lambda x:
        "Grants the player 12, 14, 16, 18, or 20 onrane.",

    "UnlockEmote": lambda x:
        "Unlocks the {} emote."
        .format(x["id"]),

    "UnlockPortal": lambda x:
        "Unlocks a {}."
        .format(x["lockedName"]),

    "UnlockSkin": lambda x:
        "Unlocks skin type {}."
        .format(x["skinType"]),

    "VampireBlast": lambda x:
        "Steals {} HP within {} tiles. Centered around the player's cursor."
        .format(x["totalDamage"], x["radius"]),

    "XPBoost": lambda x:
        "Grants a 50% loot boost for {} minutes."
        .format(int(x["duration"]) / 60)
}
