from modules.cells.Cell import Cell
from modules.Log import log


class Property(Cell):
    """Property Class (for Properties, Rails, Utilities)"""

    def __init__(self, name, cost_base, rent_base, cost_house, rent_house, group):
        self.name = name
        self.cost_base = cost_base
        self.rent_base = rent_base
        self.cost_house = cost_house
        self.rent_house = rent_house
        self.group = group
        self.owner = ""
        self.isMortgaged = False
        self.isMonopoly = False
        self.hasHouses = 0

    def action(self, player, rent, board):
        """Player ended on a property"""

        # it's their property or mortgaged - do nothing
        if self.owner == player or self.isMortgaged:
            log.write("No rent this time", 3)
            return

        # Property up for sale
        elif self.owner == "":
            if player.wantsToBuy(self.cost_base, self.group):
                log.write(player.name+" buys property " +
                          self.name + " for $"+str(self.cost_base), 3)
                player.takeMoney(self.cost_base)
                self.owner = player
                board.recalculateAfterPropertyChange()
            else:
                pass  # auction here
                log.write(player.name+" didn't buy the property.", 3)
                # Auction here
                # Decided not to implement it...
            return

        # someone else's property - pay the rent
        else:
            player.takeMoney(rent)
            self.owner.addMoney(rent)
            log.write(player.name+" pays the rent $" +
                      str(rent) + " to "+self.owner.name, 3)

    # mortgage the plot to the player / or sell the house
    def mortgage(self, player, board):
        """Sell hotel"""
        if self.hasHouses == 5:
            player.addMoney(self.cost_house * 5 // 2)
            self.hasHouses = 0
            board.nHotels -= 1
            log.write(player.name+" sells hotel on "+self.name, 3)
        # Sell one house
        elif self.hasHouses > 0:
            player.addMoney(self.cost_house // 2)
            self.hasHouses -= 1
            board.nHouses -= 1
            log.write(player.name+" sells house on "+self.name, 3)
        # Mortgage
        else:
            self.isMortgaged = True
            player.addMoney(self.cost_base // 2)
            # log name of the plot and money player need to pay to get it back
            player.hasMortgages.append(
                (self, int((self.cost_base // 2) * 1.1)))
            log.write(player.name+" mortgages "+self.name, 3)

    # unmortgage thr plot

    def unmortgage(self, player):
        # print (player.hasMortgages)
        for mortgage in player.hasMortgages:
            if mortgage[0] == self:
                thisMortgage = mortgage
        self.isMortgaged = False
        player.takeMoney(thisMortgage[1])
        player.hasMortgages.remove(thisMortgage)
        log.write(player.name+" unmortgages "+self.name, 3)
