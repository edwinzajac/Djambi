#Screen dimensions

from gettext import install
import json


WIDTH = 630 
HEIGHT = WIDTH #doit être multiple de 9
MARGIN = WIDTH//10

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

    BG_COLOR = colorsDict["background"]
    DEAD_COLOR = colorsDict["dead"]
    THRONE_BG_COLOR = colorsDict["throne"]["background"]
    P1_COLOR = colorsDict["pieces"]["red"]
    P2_COLOR = colorsDict["pieces"]["blue"]
    P3_COLOR = colorsDict["pieces"]["yellow"]
    P4_COLOR = colorsDict["pieces"]["green"]

# IMAGES
THRONE_IMG_PATH = "assets/pieces/black/crown.svg"
