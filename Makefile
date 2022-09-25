py = python3

all:
	$(py) main.py

colorize-pieces:
	$(py) assetsCreation/generateColorPieces.py assets/pieces
