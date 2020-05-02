import behavior

# get a list of every enemy behavior
path = "something/ut-core-master/server/wServer/logic/db/*.cs"
behavs = behavior.GetBehaviorsFromGlob(path)
behavs.sort(key = lambda e: e.host)

# ignore hp and mp pots
ignoredLoot = ["Health Potion", "Magic Potion"]

# write output to the output file
out = open("something/ut-utility/output/behavior-scanner.txt", "r+")
out.truncate(0)
out.write(behavior.GetLootAndPerc(behavs, lambda x: x[0] in ignoredLoot))
out.close()