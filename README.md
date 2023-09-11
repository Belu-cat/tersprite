# tersprite
WARNING! BAD CODE AHEAD

tersprite is a Python module to draw (animated) frames to a terminal screen. "main.py" in this repo is a simple example program.

## Installing
To install tersprite, open up a terminal and navigate to the desiried location. Then, run:
`git clone https://github.com/Belu-cat/tersprite/tree/main`
Copy "tersprite.py" from the "tersprite" folder and paste it where you want to use it.

## Usage
To begin, import tersprite like this:

`import tersprite`

### Sprites
Sprites are the main focus of this module. A sprite has three properties, its X pos, Y pos, and if it is hidden. Hidden sprites are not rendered. To start, create a sprite, for an example "sprite1" like this:

`tersprite.sprite("sprite1", 5, 8)`
This will make a sprite called "sprite1" and set its x and y locations to 5, 8.
Create a folder called assets, and make a file called "sprite1.txt" in it. To render this sprite, run:

`print(tersprite.render(80, 80))`
This will create an empty gird with the dimentions 80x80 charectors, and place all sprites on it. Then, it will print it to the console. Keep in mind that (due to a known bug), you will need an empty line with all spaces at the end of the "sprite1.txt" file. You also need trailing spaces on all other lines to match its dimentions. You can hide this sprite with the hide() function like this:

`hide("sprite1)`
And show it again like this:

`show("sprite1")`

## Changing defaults
By default, tersprite saves all asset files to a folder called "assets", as we mentioned before. However, you can also change the asset folder to any folder you want using the assetLoc() function. Run the following:
`assetLoc("notAssets")`
Now, all assets will have to be moved to notAssets, and tersprite will look for assets in the "notAssets" folder.