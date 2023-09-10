import tersprite
tersprite.assetLoc("assets")
# print(tersprite.assetLoc)
tersprite.sprite("default", 0, 5)
# print(tersprite.sprites)
# print(tersprite.spriteLoc("default"))
var = tersprite.deconstruct(tersprite.drawSprite("default"), 60, 60)
i = 1
while i != len(var):
    print(var[i])
    i += 1