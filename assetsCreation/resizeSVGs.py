""" SVG Resize 
This script resizes every svg in the selected folder.

Usage:
python resizeSVGs.py svgDir scale 

:svgDir: directory containing the svgs to resize

:scale: scale factor for the resize

"""

import logging
import sys
from os import listdir, getcwd, mkdir
from os.path import isfile, join
import svgutils 

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

def resizeSVGs(svgDir,scale=1.):
    """Resize all svgs in svgDir with the selected scale factor 

    :svgDir: directory containing .svg files
    :scale: scale factore
    :returns: nothing 

    """
    #Get the names of the blank svgs
    blankPiecesDir = join(svgDir,"blank")
    logger.debug(f"pieces directory -> {blankPiecesDir}")
    logger.debug(f"blank pieces directory -> {blankPiecesDir}")
    svgToResize = getNamesOfFiles(blankPiecesDir)
    logger.debug(f"files to resize -> {svgToResize})")

    for svgFile in svgToResize:
        svg = svgutils.transform.fromfile(join(blankPiecesDir,svgFile))
        originalSVG = svgutils.compose.SVG(join(blankPiecesDir,svgFile))
        originalSVG.scale(2)
        figure = svgutils.compose.Figure(float(svg.height) * scale, float(svg.width) * scale, originalSVG)
        figure.save(join(blankPiecesDir,"ok"+svgFile))


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
        message = f"Usage: {sys.argv[0]} svgDir scale"
        raise InputError(sys.argv,message)
    
    svgDir = sys.argv[1]
    scale = float(sys.argv[2])
    resizeSVGs(svgDir,scale)
