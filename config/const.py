#Screen dimensions

from gettext import install


WIDTH = 540 
HEIGHT = 540 #doit être multiple de 9

# Board dimensions

ROWS = 9
COLS = 9
SQSIZE = WIDTH // COLS

# COLORS

PRIMARY_CHECKERBOARD_COLOR = (236, 240, 241)
SECONDARY_CHECKERBOARD_COLOR = (149, 165, 166) 

piecesColorDict =  {
    #don't put 'blank' key
    "red": {
        "fillColor": "#e74c3c",
        "drawColor": "#7b190f"
        },
    "yellow": {
        "fillColor": "#f1c40f",
        "drawColor": "#614f06"
        },
    "green": {
        "fillColor": "#2ecc71",
        "drawColor": "#124f2c"
        },
    "blue": {
        "fillColor": "#3498db",
        "drawColor": "#124364"
        },
    "black": {
        "fillColor": "#1e272e",
        "drawColor": "#d2dae2"
        },
    "orange": {
        "fillColor": "#e67e22",
        "drawColor": "#64350b"
        },
    "purple": {
        "fillColor": "#8e44ad",
        "drawColor": "#34193f"
        }
}

