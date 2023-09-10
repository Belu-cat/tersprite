assetLoc = ""
sprites = {
}

sprites["default"] = {
    "x": 0,
    "y": 0,
}

def assetLoc(dir):
    global assetLoc
    if dir == "":
        return assetLoc
    else:
        assetLoc = dir

def sprite(name = "", x = "", y = ""):
    if x == "":
        return sprites[name]
    else:
        sprites[name] = {
        "x": x,
        "y": y,
    }
        
def spriteLoc(name):
    return [sprites[name]["x"], sprites[name]["y"]]

def drawSprite(name):
    global sprites
    f = open("assets/best.txt")
    sprite = f.read().split("\n")
    ofsetX = sprites[name]["x"]
    ofsetY = sprites[name]["y"]
    x = 0
    y = 0
    temp = []
    while y != len(sprite[0]) + 1:
        x = 0
        while x != len(sprite) + 1:
            temp.append([x + ofsetX, y + ofsetY, sprite[x - 1][y - 1]])
            x += 1
        y += 1
    f.close()
    return temp

def deconstruct(drawOutput, lenX, lenY):
    i = 0
    temp = []
    while i != lenX + 1:
        temp.append(" ")
        i += 1
    temp1 = "".join(temp)
    temp = []
    i = 0
    while i != lenY + 1:
        temp.append(temp1)
        i += 1
    i = 0
    while i != len(drawOutput):
        x = drawOutput[i][1]
        y = drawOutput[i][0]
        char = drawOutput[i][2]
        temp1 = list(temp[y])
        temp1[x] = char
        temp[y] = "".join(temp1)
        i += 1
    return temp