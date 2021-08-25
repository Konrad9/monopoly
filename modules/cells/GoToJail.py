from modules.cells.Cell import Cell
from modules.Log import log


class GoToJail(Cell):
    """Go to Jail (#30)"""

    def action(self, player):
        player.moveTo(10)
        player.inJail = True
        log.write(player.name+" goes to jail from Go To Jail ", 3)
