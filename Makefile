py = python3

all:
	$(py) main.py

requirements:
	$(py) -m pip install -r requirements.txt

colorize-pieces:
	$(py) assetsCreation/generateColorPieces.py assets/pieces

