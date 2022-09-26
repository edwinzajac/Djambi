[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
# Djambi Project

## Assets

| Chief                                     | Assassin | Diplomat | Necromobile| Reporter                                     | militant | 
|:------------------------------------------|:---------|:---------|:------------|:---------|:---------------------------------------------|
| <img src="./assets/pieces/black/chief.svg"> | <img src="./assets/pieces/black/assassin.svg">|<img src="./assets/pieces/black/diplomat.svg">| <img src="./assets/pieces/black/necromobile.svg">| <img src="./assets/pieces/black/reporter.svg">|  <img src="./assets/pieces/black/militant.svg">         | 
| <img src="./assets/pieces/red/chief.svg"> | <img src="./assets/pieces/red/assassin.svg">|<img src="./assets/pieces/red/diplomat.svg">| <img src="./assets/pieces/red/necromobile.svg">| <img src="./assets/pieces/red/reporter.svg">|  <img src="./assets/pieces/red/militant.svg">         | 
| <img src="./assets/pieces/orange/chief.svg"> | <img src="./assets/pieces/orange/assassin.svg">|<img src="./assets/pieces/orange/diplomat.svg">| <img src="./assets/pieces/orange/necromobile.svg">| <img src="./assets/pieces/orange/reporter.svg">|  <img src="./assets/pieces/orange/militant.svg">         | 
| <img src="./assets/pieces/yellow/chief.svg"> | <img src="./assets/pieces/yellow/assassin.svg">|<img src="./assets/pieces/yellow/diplomat.svg">| <img src="./assets/pieces/yellow/necromobile.svg">| <img src="./assets/pieces/yellow/reporter.svg">|  <img src="./assets/pieces/yellow/militant.svg">         | 
| <img src="./assets/pieces/green/chief.svg"> | <img src="./assets/pieces/green/assassin.svg">|<img src="./assets/pieces/green/diplomat.svg">| <img src="./assets/pieces/green/necromobile.svg">| <img src="./assets/pieces/green/reporter.svg">|  <img src="./assets/pieces/green/militant.svg">         | 
| <img src="./assets/pieces/blue/chief.svg"> | <img src="./assets/pieces/blue/assassin.svg">|<img src="./assets/pieces/blue/diplomat.svg">| <img src="./assets/pieces/blue/necromobile.svg">| <img src="./assets/pieces/blue/reporter.svg">|  <img src="./assets/pieces/blue/militant.svg">         | 
| <img src="./assets/pieces/purple/chief.svg"> | <img src="./assets/pieces/purple/assassin.svg">|<img src="./assets/pieces/purple/diplomat.svg">| <img src="./assets/pieces/purple/necromobile.svg">| <img src="./assets/pieces/purple/reporter.svg">|  <img src="./assets/pieces/purple/militant.svg">         | 

## Structure

```mermaid
classDiagram
class AbstractBoard{
       boardMatrix 
bool centerIsOccupied
possibleNbPlayers=[]
       __init__()
       getPossibleMoves(self,piece,origincell)
       move(self,origincell,destcell)
}
class HexaBoard{possibleNbPlayers=[2,4]
__init__(self)}
class SquareBoard{
__init__(self)
possibleNbPlayers=[3,6]}
class Game{
 int currentPlayer 
 AbstractBoard gameBoard 
 nextPlayer()
 ...}
class Player{
string name
string color
int order
}
class Cell {
int coordQ
int coordS
int coordR
Piece piece
isCenter()
}
class Piece {
Image img
string name
string description
}
AbstractBoard <|-- HexaBoard
AbstractBoard <|-- SquareBoard

AbstractBoard "1" -- "1"Game
Game "1" -- "2..6" Player
AbstractBoard "1" -- "*" Cell
Cell "*" -- "1" Piece
```

## Make Commands

### Run game

```shell
make
```

### Install requirements 

```shell
make requirements
```

### Generate colorized assets 

```shell
make colorize-pieces 
```
