from modules.cells.Cell import Cell
from settings.data import *
from modules.Log import log


class Chance(Cell):
    """Chance cards"""

    def action(self, player, board):

        # Get the card
        chanceCard = board.chanceCards.pop(0)

        # Actions for various cards

        # 0: Advance to St.Charle
        if chanceCard == 0:
            log.write(player.name+" gets chance card: Advance to St.Charle's", 3)
            if player.position >= 11:
                player.addMoney(settingsSalary)
                log.write(player.name+" gets salary: $"+str(settingsSalary), 3)
            player.position = 11
            log.write(player.name+" goes to "+str(board.b[11].name), 3)
            board.action(player, player.position)

        # 1: Get Out Of Jail Free
        elif chanceCard == 1:
            log.write(player.name+" gets chance card: Get Out Of Jail Free", 3)
            player.hasJailCardChance = True

        # 2: Take a ride on the Reading
        elif chanceCard == 2:
            log.write(
                player.name+" gets chance card: Take a ride on the Reading", 3)
            if player.position >= 5:
                player.addMoney(settingsSalary)
                log.write(player.name+" gets salary: $"+str(settingsSalary), 3)
            player.position = 5
            log.write(player.name+" goes to " +
                      str(board.b[player.position].name), 3)
            board.action(player, player.position)

        # 3: Move to the nearest railroad and pay double
        elif chanceCard == 3:
            log.write(
                player.name+" gets chance card: Move to the nearest railroad and pay double", 3)
            # Don't get salary, even if you pass GO (card doesnt say to do it)
            # Dont move is already on a rail.
            # Also, I assue advance means you should go to the nearest in fron of you, not behind
            player.position = ((player.position+4)//10*10 +
                               5) % 40  # nearest railroad
            # twice for double rent, if needed
            board.action(player, player.position, special="from_chance")

        # 4: Advance to Illinois Avenue
        elif chanceCard == 4:
            log.write(
                player.name+" gets chance card: Advance to Illinois Avenue", 3)
            if player.position >= 24:
                player.addMoney(settingsSalary)
                log.write(player.name+" gets salary: $"+str(settingsSalary), 3)
            player.position = 24
            log.write(player.name+" goes to " +
                      str(board.b[player.position].name), 3)
            board.action(player, player.position)

        # 5: Make general repairs to your property
        elif chanceCard == 5:
            log.write(
                player.name+" gets chance card: Make general repairs to your property", 3)
            player.makeRepairs(board, "chance")

        # 6: Advance to GO
        elif chanceCard == 6:
            log.write(player.name+" gets chance card: Advance to GO", 3)
            player.addMoney(settingsSalary)
            log.write(player.name+" gets salary: $"+str(settingsSalary), 3)
            player.position = 0
            log.write(player.name+" goes to " +
                      str(board.b[player.position].name), 3)

        # 7: Bank pays you dividend $50
        elif chanceCard == 7:
            log.write(
                player.name+" gets chance card: Bank pays you dividend $50", 3)
            player.addMoney(50)

        # 8: Pay poor tax $15
        elif chanceCard == 8:
            log.write(player.name+" gets chance card: Pay poor tax $15", 3)
            player.takeMoney(15)

        # 9: Advance to the nearest Utility and pay 10x dice
        elif chanceCard == 9:
            log.write(
                player.name+" gets chance card: Advance to the nearest Utility and pay 10x dice", 3)
            if player.position > 12 and player.position <= 28:
                player.position = 28
            else:
                player.position = 12
            board.action(player, player.position, special="from_chance")

        # 10: Go Directly to Jail
        elif chanceCard == 10:
            log.write(player.name+" gets chance card: Go Directly to Jail", 3)
            player.moveTo(10)
            player.inJail = True
            log.write(player.name+" goes to jail on Chance card", 3)

        # 11: You've been elected chairman. Pay each player $50
        elif chanceCard == 11:
            log.write(
                player.name+" gets chance card: You've been elected chairman. Pay each player $50", 3)
            for other_player in board.players:
                if other_player != player and not other_player.isBankrupt:
                    player.takeMoney(50)
                    other_player.addMoney(50)

        # 12: Advance to BoardWalk
        elif chanceCard == 12:
            log.write(player.name+" gets chance card: Advance to BoardWalk", 3)
            player.position = 39
            log.write(player.name+" goes to " +
                      str(board.b[player.position].name), 3)
            board.action(player, player.position)

        # 13: Go back 3 spaces
        elif chanceCard == 13:
            log.write(player.name+" gets chance card: Go back 3 spaces", 3)
            player.position -= 3
            log.write(player.name+" goes to " +
                      str(board.b[player.position].name), 3)
            board.action(player, player.position)

        # 14: Your building loan matures. Receive $150.
        elif chanceCard == 14:
            log.write(
                player.name+" gets chance card: Your building loan matures. Receive $150", 3)
            player.addMoney(150)

        # 15: You have won a crossword competition. Collect $100
        elif chanceCard == 15:
            log.write(
                player.name+" gets chance card: You have won a crossword competition. Collect $100", 3)
            player.addMoney(100)

        # Put the card back
        if chanceCard != 1:  # except GOOJF card
            board.chanceCards.append(chanceCard)
