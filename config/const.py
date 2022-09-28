#Screen dimensions

from gettext import install
import json


WIDTH = 630 
HEIGHT = 630 #doit être multiple de 9

# Board dimensions

ROWS = 9
COLS = 9
SQSIZE = WIDTH // COLS

# COLORS
with open("config/colors.json","r") as colorsJson:
    colorsDict = json.load(colorsJson)

    POSSIBLE_MOVE_COLOR = colorsDict["possible_moves"]
    PRIMARY_CHECKERBOARD_COLOR = colorsDict["checker_board"]["PRIMARY"] 
    SECONDARY_CHECKERBOARD_COLOR = colorsDict["checker_board"]["SECONDARY"]

    P1_COLOR = colorsDict["pieces"]["red"]
    P2_COLOR = colorsDict["pieces"]["blue"]
    P3_COLOR = colorsDict["pieces"]["yellow"]
    P4_COLOR = colorsDict["pieces"]["green"]
