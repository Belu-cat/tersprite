import os
assetLoc = "assets"
sprites = {
}

spriteList = ["default"]

switches = {
    "inputEveryFrame?": False
}

sprites["default"] = {
    "x": 0,
    "y": 0,
    "asset": "best.txt",
    "show?": True
}

def assetLoc(dir):
    global assetLoc
    if dir == "":
        return assetLoc
    else:
        assetLoc = dir

def sprite(name = "", x = "", y = "", show=True):
    if x == "":
        return sprites[name]
    else:
        sprites[name] = {
        "x": x,
        "y": y,
        "show?": show
    }
    sprites[name]["asset"] = name + ".txt"
    
    if not name in spriteList:
        spriteList.append(name)


def spriteLoc(name):
    return [sprites[name]["x"], sprites[name]["y"]]

def drawSprite(name, clearTemp = False, globalTemp = True):
    global sprites
    f = open("assets/" + sprites[name]["asset"])
    sprite = f.read().split("\n")
    ofsetX = sprites[name]["x"]
    ofsetY = sprites[name]["y"]
    x = 0
    y = 0
    if globalTemp:
        global output
    if clearTemp:
        output = []
    while y != len(sprite[0]) + 1:
        x = 0
        while x != len(sprite) + 1:
            output.append([x + ofsetX, y + ofsetY, sprite[x - 1][y - 1]])
            x += 1
        y += 1
    f.close()
    return output

def deconstruct(drawOutput, lenX, lenY, escape="\\"):
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    i = 0
    deconstruct = []
    while i != lenX:
        deconstruct.append(" ")
        i += 1
    joinDeconstruct = "".join(deconstruct)
    deconstruct = []
    i = 0
    while i != lenY:
        deconstruct.append(joinDeconstruct)
        i += 1
    i = 0
    while i != len(drawOutput):
        x = drawOutput[i][1]
        y = drawOutput[i][0]
        char = drawOutput[i][2]
        temp5 = char != " "
        temp6 = char != escape
        if  temp5 & temp6:
            joinDeconstruct = list(deconstruct[y])
            joinDeconstruct[x] = char
            deconstruct[y] = "".join(joinDeconstruct)
        elif char == escape:
            joinDeconstruct = list(deconstruct[y])
            joinDeconstruct[x] = " "
            deconstruct[y] = "".join(joinDeconstruct)
        i += 1
    return deconstruct

def spriteAsset(name, asset):
    sprites[name]["asset"] = asset

def draw():
    i2 = 0
    global output
    output = []
    while i2 != len(spriteList) + 1:
        if sprites[spriteList[i2 - 1]]["show?"]:
            combiniedOutput = drawSprite(spriteList[i2 - 1])
        i2 += 1
    return combiniedOutput

def hide(name):
    sprites[name]["show?"] = False

def show(name):
    sprites[name]["show?"] = True

def printDeconstructed(deconsructed):
    i = 0
    totalToPrint = ""
    while i != len(deconsructed):
       totalToPrint = totalToPrint + deconsructed[i] + "\n"
       i += 1
    return totalToPrint

def render(lenX, lenY):
    return(printDeconstructed(deconstruct(draw(), lenX, lenY)))