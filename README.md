[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# Djambi Project

## Assets

| Chief                                     | Assassin | Diplomat | Necromobile| Reporter                                     | Militant | Crown |
|:------------------------------------------|:---------|:---------|:------------|:---------|:---------------------------------------------|:-------|
| <img src="./assets/images/pieces/black/chief.svg"> | <img src="./assets/images/pieces/black/assassin.svg">|<img src="./assets/images/pieces/black/diplomat.svg">| <img src="./assets/images/pieces/black/necromobile.svg">| <img src="./assets/images/pieces/black/reporter.svg">|  <img src="./assets/images/pieces/black/militant.svg">         |  <img src="./assets/images/pieces/black/crown.svg">         | 
| <img src="./assets/images/pieces/red/chief.svg"> | <img src="./assets/images/pieces/red/assassin.svg">|<img src="./assets/images/pieces/red/diplomat.svg">| <img src="./assets/images/pieces/red/necromobile.svg">| <img src="./assets/images/pieces/red/reporter.svg">|  <img src="./assets/images/pieces/red/militant.svg">         |   <img src="./assets/images/pieces/red/crown.svg">         |
| <img src="./assets/images/pieces/orange/chief.svg"> | <img src="./assets/images/pieces/orange/assassin.svg">|<img src="./assets/images/pieces/orange/diplomat.svg">| <img src="./assets/images/pieces/orange/necromobile.svg">| <img src="./assets/images/pieces/orange/reporter.svg">|  <img src="./assets/images/pieces/orange/militant.svg">         |   <img src="./assets/images/pieces/orange/crown.svg">         |
| <img src="./assets/images/pieces/yellow/chief.svg"> | <img src="./assets/images/pieces/yellow/assassin.svg">|<img src="./assets/images/pieces/yellow/diplomat.svg">| <img src="./assets/images/pieces/yellow/necromobile.svg">| <img src="./assets/images/pieces/yellow/reporter.svg">|  <img src="./assets/images/pieces/yellow/militant.svg">         |   <img src="./assets/images/pieces/yellow/crown.svg">         |
| <img src="./assets/images/pieces/green/chief.svg"> | <img src="./assets/images/pieces/green/assassin.svg">|<img src="./assets/images/pieces/green/diplomat.svg">| <img src="./assets/images/pieces/green/necromobile.svg">| <img src="./assets/images/pieces/green/reporter.svg">|  <img src="./assets/images/pieces/green/militant.svg">         |   <img src="./assets/images/pieces/green/crown.svg">         |
| <img src="./assets/images/pieces/blue/chief.svg"> | <img src="./assets/images/pieces/blue/assassin.svg">|<img src="./assets/images/pieces/blue/diplomat.svg">| <img src="./assets/images/pieces/blue/necromobile.svg">| <img src="./assets/images/pieces/blue/reporter.svg">|  <img src="./assets/images/pieces/blue/militant.svg">         |   <img src="./assets/images/pieces/blue/crown.svg">         |
| <img src="./assets/images/pieces/purple/chief.svg"> | <img src="./assets/images/pieces/purple/assassin.svg">|<img src="./assets/images/pieces/purple/diplomat.svg">| <img src="./assets/images/pieces/purple/necromobile.svg">| <img src="./assets/images/pieces/purple/reporter.svg">|  <img src="./assets/images/pieces/purple/militant.svg">         |   <img src="./assets/images/pieces/purple/crown.svg">       |


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
