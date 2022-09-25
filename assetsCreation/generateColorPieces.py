""" DiBISO Page Scraper
This script allows the user to get the text data from the selected pages.

Usage:
python pageScraper.py subdirectoriesFile outputFile

:subdirectoriesFile: the file containing the list of subdirectories 
(1 on each line) corresponding to the selected pages

:outputFile: the output file where the data will be stored in json format

Three things are assumed:
- the main content is in a div with the class 'main-content'
- the base url is 'https://www.bibliotheques.universite-paris-saclay.fr'
- the title of the page is the first line of the main content
"""

import logging
import sys
from os import listdir, getcwd, mkdir
from os.path import isfile, join

## LOGGING
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

## VARIABLES
colorsDict = {
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
        }
}

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
            with open(join(colorDir,f),"w") as svg:
                svg.write(dataSvg.format(
                    fillColor=colorsDict[color]["fillColor"],
                    drawColor=colorsDict[color]["drawColor"]
                ))
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
    if len(sys.argv)!=2:
        message = f"Usage: {sys.argv[0]} piecesDir"
        raise InputError(sys.argv,message)
    #BASE_DIR = getcwd() 
    #assetsDir = join(BASE_DIR,"assets")
    #piecesDir = join(assetsDir,"pieces")
    piecesDir = sys.argv[1]
    colorizeSVGs(piecesDir,colorsDict)
