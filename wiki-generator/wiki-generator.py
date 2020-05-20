import behaviors.behavior as behavior
from items.item import GetItems
from items.itemtypes import SlotToCategory, SlotToSlotType, SlotPluralize
import utils


ITEMS_TO_EXCLUDE = []
basePath = "something"


class WikiGenerator:

    behavs = None
    enemyDropsList = None
    dropLocations = None
    items = None

    def __init__(this, utPath, exclude=[]):
        this.behavs = behavior.GetBehaviorsFromGlob(utPath + "/wServer/logic/db/*.cs")
        this.enemyDropsList = behavior.GetAllDrops(this.behavs)
        this.dropLocations = behavior.GetLootAndEnemyPerc(this.behavs)

        cond = lambda x: x.Id not in exclude and (x.GodSlayer or x.Godly or x.Sacred or x.Legendary or x.Fabled or x.RT or (x.Untiered and x.Id in this.enemyDropsList))
        this.items = GetItems(utPath + "/common/resources/xmls/client/dat1.xml", cond=cond)
        this.items.sort(key = lambda x: x.Id)

    def FormatItem(this, it):
        loc = this.dropLocations.get(it.Id, None)
        if (loc != None):
            locs = ["\nDrops from:"]
            for l in loc:
                locs.append(l[0] + ": " + str(l[1]) + "%" + utils.percentToRate(l[1]) + " chance.")
            locs.sort()
            return str(it) + "\n".join(locs) + "\n"
        else:
            return str(it) + "\nDoes not drop from enemies.\n"

    def FormatHTML(this, item, indentLevel=2):
        indent = "  " * indentLevel
        ret = indent + "<details class=\"wikiItem\" id=\"" + item.Id + "\">\n"
        ret += indent + "  <summary>" + item.Id + "</summary>\n"
        ret += indent + "</details>"
        return ret

    def FormatHTMLBig(this, cats, indentLevel=0):
        ret = ""
        idt = "  " * indentLevel
        for cat in cats:
            case = SlotPluralize(cat).replace("-", " ").title()
            ret += idt + "<details class=\"cat\" id=\"" + cat + "\">\n"
            ret += idt + "  <summary>" + case + "</summary>\n"
            for typ in cats[cat]:
                if typ != cat:
                    tCase = SlotPluralize(typ).replace("-", " ").title()
                    ret += idt + "  <details class=\"typ\" id=\"" + typ + "\">\n"
                    ret += idt + "    <summary>" + tCase + "</summary>\n"

                ret += "\n".join(cats[cat][typ]) + "\n"

                if typ != cat:
                    ret += idt + "  </details>\n"
            ret += idt + "</details>\n"
        return ret

    def PrintItemsToFile(this, path):
        lout = []
        for it in this.items:
            lout.append(this.FormatItem(it))

        wikiOut = "\n==================\n\n".join(lout)

        fout = open(path, "w")
        fout.write(wikiOut)
        fout.close()

    def PrintHTMLToFile(this, path):
        lout = []
        cats = {} # Dictionary<slotCategory, Dictionary<slotType, List<itemDetails>>>
        for x in SlotToSlotType.items():
            cat = SlotToCategory[x[0]]
            if (cat not in cats):
                cats[cat] = {x[1]: []}
            else:
                cats[cat][x[1]] = []

        for it in this.items:
            itHtml = this.FormatHTML(it)
            cats[SlotToCategory[it.SlotType]] [SlotToSlotType[it.SlotType]].append(itHtml)

        hOut = this.FormatHTMLBig(cats)

        fout = open(path, "w")
        fout.write(hOut)
        fout.close()

    def MakeDirs(this, path):
        import os
        if (not os.path.isdir(path)):
            raise Exception("Directory does not exist: \"" + path + "\".")

        for x in SlotToCategory.items():
            if (x[1] != SlotToSlotType[x[0]]):
                os.makedirs(path + "/" + x[1] + "/" + SlotToSlotType[x[0]], exist_ok=True)
            else:
                os.makedirs(path + "/" + x[1], exist_ok=True)

    def MakeWiki(this, path, makeTree=True):
        if (makeTree):
            this.MakeDirs(path)
        for it in this.items:
            sCat = SlotToCategory[it.SlotType]
            sTyp = SlotToSlotType[it.SlotType]
            extPath = ""
            if (makeTree):
                extPath = "/" + sCat if sCat == sTyp else "/" + sCat + "/" + sTyp
            itFile = utils.FormatFileName(it.Id, "txt") 

            fout = open(path + extPath + "/" + itFile, "w")
            fout.write(this.FormatItem(it))
            fout.close()

if (__name__ == "__main__"):
    wg = WikiGenerator(basePath + "/ut-v4-source-master/ut-core-master/server", exclude=ITEMS_TO_EXCLUDE)
    wg.PrintHTMLToFile(basePath + "/ut-utility/output/xml-parser.txt")
    wg.MakeWiki(basePath + "/ut-utility/output/wiki/all", makeTree=False)
