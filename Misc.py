##MISC FUNCTIONS


def pad0s(string, modulo):
    while len(string) % modulo != 0:
        string = "0" + string
    return string

def bitSplit32(string):
    count = 0
    add = ""
    l1 = []
    for x in string:
        add += x
        count += 1
        if count == 2:
           l1.append(add)
           add = ""
           count = 0
    return l1

def bitJoin32(mList):
    resultString = ""
    for x in mList:
        resultString += x
    return resultString
