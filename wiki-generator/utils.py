
def firstBetween(src, separator):
    ''' Params: string src, string separator
        Returns: string
        Returns an empty string or the string between the first and second occurrences of the separator parameter in the src parameter.
        '''
    startPos = src.find(separator) + 1
    if (startPos == -1):
        return ""
    endPos = src.find(separator, startPos)
    if (endPos == -1):
        return ""
    return src[startPos:endPos]

def firstString(src):
    ''' Params: string src
        Returns: string
        Returns an empty string or the first string found in the source code from parameter src. Removes quotation marks.
        '''
    return firstBetween(src, "\"")

def afterFirst(src, txt):
    ''' Params: string src, string txt
        Returns: string
        Returns an empty string or a string with everything before and including the first occurence of the txt parameter removed from the src parameter.
        '''
    startPos = src.find(txt)
    if (startPos == -1):
        return ""
    return src[startPos + len(txt):]

def beforeFirst(src, txt):
    ''' Params: string src, string txt
        Returns: string
        Returns an empty string or  a string with everything after and including the first occurence of the txt parameter removed from the src parameter.
        '''
    startPos = src.find(txt)
    if (startPos == -1):
        return ""
    return src[:startPos]

def firstNumber(src):
    ''' Params: string src
        Returns: float
        Returns the first number from the src parameter or 0 if there is no number.
        '''
    if (len(src) == 0):
        return 0

    for x in range(len(src)):
        if src[x].isdigit():
            return fullNumberFromIndex(src, x)

    return 0

def fullNumberFromIndex(src, idx):
    ''' Params: string src, int idx
        Returns: float
        Returns a float parsed from the src param starting at index idx. If the character before src[idx] is "." then it will be used as the start of the return value.
        '''
    dec = False
    if (idx > 0 and src[idx - 1] == "."):
        idx -= 1

    for x in range(idx, len(src)):
        c = src[x]
        if not c.isdigit():
            if (not dec) and c == ".":
                dec = True
                continue
            else:
                return float(src[idx:x])
    
    return float(src[idx:])

def percentToRate(x):
    ''' Params: float x
        Returns: string
        Returns a string with drop rate percentage x converted to 1/number format, or an empty string if x is >= 40.0
        '''
    if (x >= 40.0):
        return ""
    return " (1/" + str(int(100/x)) + ")"

def FormatFileName(name, ext):
    ''' Params: string name, string ext
        Returns: string
        Returns a valid file name with file extension ext. Removes whitespace, commas, etc from name and makes name lowercase.
        '''
    newName = name.lower().replace(" ", "-").replace("_", "-")
    for ch in newName:
        if (not (ch.isalnum() or ch == "-")):
            newName = newName.replace(ch, "")
    return newName + "." + ext
