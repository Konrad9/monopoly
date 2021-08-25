from modules.cells.Cell import Cell
from modules.Log import log
from settings.data import *


class PropertyTax(Cell):
    """Pay Property Tax cell (200 or 10%) (#4)"""

    def action(self, player, board):
        toPay = min(settingsPropertyTax, player.netWorth(board)//10)
        log.write(player.name+" pays Property Tax $"+str(toPay), 3)
        player.takeMoney(toPay)
