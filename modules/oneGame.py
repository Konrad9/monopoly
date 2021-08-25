from modules.Player import Player
from modules.Board import Board
from settings.data import *
import util
import random
from modules.Log import log


def isGameOver(players):
    """Check if there are more then 1 player left in the game"""
    alive = 0
    for player in players:
        if not player.isBankrupt:
            alive += 1
    if alive > 1:
        return False
    else:
        return True

# simulate one game


def oneGame():

    # create players
    players = []
    # names = ["pl"+str(i) for i in range(nPlayers)]
    names = [util.cardinal(i + 1) for i in range(nPlayers)]
    if shufflePlayers:
        random.shuffle(names)
    for i in range(nPlayers):
        if variableStartingMoney == []:
            startingMoney = settingStartingMoney
        else:
            startingMoney = variableStartingMoney[i]
        players.append(Player(names[i], startingMoney))

    # create board
    gameBoard = Board(players)

    #  netWorth history first point
    if writeData == "netWorth":
        networthstring = ""
        for player in players:
            networthstring += str(player.netWorth(gameBoard))
            if player != players[-1]:
                networthstring += "\t"
        log.write(networthstring, data=True)

    # game
    for i in range(nMoves):
        if realTime:
            input("Press enter to continue")
        if isGameOver(players):
            # to track length of the game
            if writeData == "lastTurn":
                log.write(str(i-1), data=True)
            break

        log.write("TURN "+str(i+1), 1)
        for player in players:
            if player.money > 0:
                log.write(
                    f"{f'{player.name}: ':8} ${player.money} | position:"+str(player.position), 2)

        for player in players:
            if not isGameOver(players):  # Only continue if 2 or more players
                # returns True if player has to go again
                while player.makeAMove(gameBoard):
                    pass

        # track netWorth history of the game
        if writeData == "netWorth":
            networthstring = ""
            for player in players:
                networthstring += str(player.netWorth(gameBoard))
                if player != players[-1]:
                    networthstring += "\t"
            log.write(networthstring, data=True)

    # tests
# for player in players:
# player.threeWayTrade(gameBoard)

    # return final scores
    results = [players[i].getMoney() for i in range(nPlayers)]

    # if it is an only simulation, print map and final score
    if nSimulations == 1 and showMap:
        gameBoard.printMap()
    if nSimulations == 1 and showResult:
        print(results)
    return results
