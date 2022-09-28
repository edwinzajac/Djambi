""" SVG Generator for pieces 
This script generates the svgs corresponding to the colored pieces of the game.

Usage:
python generateColorPieces.py piecesDir colorsFile.json

:piecesDir: the pieces folder containing a folder for each color, 'blank' being
the one containing all non formated svgs with {fillColor} and 
{drawColor} to replace

:colorsFile.json: json file containing the key 'pieces' for the colors
dictionnary

"""

import logging
import sys
import json
from os import listdir, getcwd, mkdir
from os.path import isfile, join

## LOGGING
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

## VARIABLES

def getNamesOfFiles(directory):
    """Return the list of the files in the directory 

    :directory: directory path string 
    :returns: list of the files in the directory 

    """
    return [f for f in listdir(directory) if isfile(join(directory, f))]

def colorizeSVGs(piecesDir,colorsDict):
    """Create colorized svgs from originDirectory and save them


    :piecesDir: directory where svg to be colorized are stored 
    :colorsDict: dict containing the color parameters 
    :returns: nothing 

    """
    #Get the names of the blank svgs
    blankPiecesDir = join(piecesDir,"blank")
    logger.debug(f"pieces directory -> {piecesDir}")
    logger.debug(f"blank pieces directory -> {blankPiecesDir}")
    svgToColorize = getNamesOfFiles(blankPiecesDir)
    logger.debug(f"files to colorize -> {svgToColorize})")

    #for each color category in the colors dictionnary
    for color in colorsDict.keys():

        #create the corresponding folder if it doesn't exists
        colorDir = join(piecesDir,color)
        try:
            mkdir(colorDir)
            logger.debug(f"{colorDir} directory created successfully")
        except FileExistsError:
            logger.debug(f"{colorDir} directory already exists")

        #colorize each blank svg with the specified colors in the dictionnary
        for f in svgToColorize:
            with open(join(blankPiecesDir,f),"r") as svg:
                dataSvg = svg.read()
            coloredSvg = dataSvg.format(
                    **colorsDict[color]
                )
            with open(join(colorDir,f),"w") as svg:
                svg.write(coloredSvg)
                logger.debug(f"{svg.name} saved")

class InputError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

if __name__ == "__main__":
    if len(sys.argv)!=3:
        message = f"Usage: {sys.argv[0]} piecesDir colors.json"
        raise InputError(sys.argv,message)
    #BASE_DIR = getcwd() 
    #assetsDir = join(BASE_DIR,"assets")
    #piecesDir = join(assetsDir,"pieces")
    
    piecesDir = sys.argv[1]
    colorsJsonFile = sys.argv[2]
    with open(colorsJsonFile,"r") as colorsJson:
        colorsDict = json.load(colorsJson)
        colorizeSVGs(piecesDir,colorsDict["pieces"])
