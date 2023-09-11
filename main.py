import tersprite
import os
tersprite.assetLoc("assets")
# print(tersprite.assetLoc)
tersprite.sprite("default", 5, 5)
tersprite.spriteAsset("default", "best.txt")
tersprite.sprite("numbertwo", 7, 9)
# print(tersprite.sprites)
# print(tersprite.spriteLoc("default"))
var = tersprite.deconstruct(tersprite.draw(), 30, 25)

i = 0
while i != len(var):
    print(var[i])
    i += 1