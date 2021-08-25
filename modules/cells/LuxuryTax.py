from modules.cells.Cell import Cell
from modules.Log import log
from settings.data import *


class LuxuryTax(Cell):
    """Pay Luxury Tax cell (#38)"""

    def action(self, player):
        player.takeMoney(settingsLuxuryTax)
        log.write(player.name+" pays Luxury Tax $"+str(settingsLuxuryTax), 3)
