#Screen dimensions

from gettext import install
import json


WIDTH = 540 
HEIGHT = 540 #doit être multiple de 9

# Board dimensions

ROWS = 9
COLS = 9
SQSIZE = WIDTH // COLS

# COLORS

PRIMARY_CHECKERBOARD_COLOR = (236, 240, 241)
SECONDARY_CHECKERBOARD_COLOR = (149, 165, 166) 
with open("config/colors.json","r") as colorsJson:
    colorsDict = json.load(colorsJson)

PRIMARY_CHECKERBOARD_COLOR = colorsDict["checker_board"]["PRIMARY"] 
SECONDARY_CHECKERBOARD_COLOR = colorsDict["checker_board"]["SECONDARY"]
