import tersprite
import os
tersprite.assetLoc("assets")
# print(tersprite.assetLoc)
tersprite.sprite("default", 0, 5)
# print(tersprite.sprites)
# print(tersprite.spriteLoc("default"))
var = tersprite.deconstruct(tersprite.drawSprite("default"), 30, 25)
i = 1
while i != len(var):
    print(var[i])
    i += 1