import os
assetLoc = ""
sprites = {
}

spriteList = ["default"]

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
        global temp
    if clearTemp:
        temp = []
    while y != len(sprite[0]) + 1:
        x = 0
        while x != len(sprite) + 1:
            temp.append([x + ofsetX, y + ofsetY, sprite[x - 1][y - 1]])
            x += 1
        y += 1
    f.close()
    return temp

def deconstruct(drawOutput, lenX, lenY, escape="\\"):
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    i = 0
    temp = []
    while i != lenX:
        temp.append(" ")
        i += 1
    temp1 = "".join(temp)
    temp = []
    i = 0
    while i != lenY:
        temp.append(temp1)
        i += 1
    i = 0
    while i != len(drawOutput):
        x = drawOutput[i][1]
        y = drawOutput[i][0]
        char = drawOutput[i][2]
        if char != " ":
            temp1 = list(temp[y])
            temp1[x] = char
            temp[y] = "".join(temp1)
        elif char == escape:
            temp1 = list(temp[y])
            temp1[x] = " "
            temp[y] = "".join(temp1)
        i += 1
    return temp

def spriteAsset(name, asset):
    sprites[name]["asset"] = asset

def draw():
    i2 = 0
    global temp
    temp = []
    while i2 != len(spriteList) + 1:
        if sprites[spriteList[i2 - 1]]["show?"]:
            temp1 = drawSprite(spriteList[i2 - 1])
        i2 += 1
    return temp1

def hide(name):
    sprites[name]["show?"] = False

def show(name):
    sprites[name]["show?"] = True