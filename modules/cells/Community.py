from modules.cells.Cell import Cell
from modules.Log import log
from settings.data import *


class Community(Cell):
    """Community Chest cards"""

    def action(self, player, board):

        # Get the card
        communityCard = board.communityCards.pop(0)

        # Actions for various cards

        # 0: Pay school tax $150
        if communityCard == 0:
            log.write(player.name+" gets community card: Pay school tax $150", 3)
            player.takeMoney(150)

        # 1: Opera night: collect $50 from each player
        if communityCard == 1:
            log.write(player.name+" Opera night: collect $50 from each player", 3)
            for other_player in board.players:
                if other_player != player and not other_player.isBankrupt:
                    player.addMoney(50)
                    other_player.takeMoney(50)
                    other_player.checkBankrupcy(board)

        # 2: You inherit $100
        if communityCard == 2:
            log.write(player.name+" gets community card: You inherit $100", 3)
            player.addMoney(100)

        # 3: Pay hospital $100
        if communityCard == 3:
            log.write(player.name+" gets community card: Pay hospital $100", 3)
            player.takeMoney(100)

        # 4: Income tax refund $20
        if communityCard == 4:
            log.write(
                player.name+" gets community card: Income tax refund $20", 3)
            player.addMoney(20)

        # 5: Go Directly to Jail
        elif communityCard == 5:
            log.write(player.name+" gets community card: Go Directly to Jail", 3)
            player.moveTo(10)
            player.inJail = True
            log.write(player.name+" goes to jail on Community card", 3)

        # 6: Get Out Of Jail Free
        elif communityCard == 6:
            log.write(player.name+" gets community card: Get Out Of Jail Free", 3)
            player.hasJailCardCommunity = True

        # 7: Second prize in beauty contest $10
        if communityCard == 7:
            log.write(
                player.name+" gets community card: Second prize in beauty contest $10", 3)
            player.addMoney(10)

        # 8: You are assigned for street repairs
        elif communityCard == 8:
            log.write(
                player.name+" gets community card: You are assigned for street repairs", 3)
            player.makeRepairs(board, "community")

        # 9: Bank error in your favour: $200
        if communityCard == 9:
            log.write(
                player.name+" gets community card: Bank error in your favour: $200", 3)
            player.addMoney(200)

        # 10: Advance to GO
        elif communityCard == 10:
            log.write(player.name+" gets community card: Advance to GO", 3)
            player.addMoney(settingsSalary)
            log.write(player.name+" gets salary: $"+str(settingsSalary), 3)
            player.position = 0
            log.write(player.name+" goes to " +
                      str(board.b[player.position].name), 3)

        # 11: X-Mas fund matured: $100
        if communityCard == 11:
            log.write(
                player.name+" gets community card: X-Mas fund matured: $100", 3)
            player.addMoney(100)

        # 12: Doctor's fee $50
        if communityCard == 12:
            log.write(player.name+" gets community card: Doctor's fee $50", 3)
            player.takeMoney(50)

        # 13: From sale of stock you get $45
        if communityCard == 13:
            log.write(
                player.name+" gets community card: From sale of stock you get $45", 3)
            player.addMoney(45)

        # 14: Receive for services $25
        if communityCard == 14:
            log.write(
                player.name+" gets community card: Receive for services $25", 3)
            player.addMoney(25)

        # 15: Life insurance matures, collect $100
        if communityCard == 15:
            log.write(
                player.name+" gets community card: Life insurance matures, collect $100", 3)
            player.addMoney(100)

        # Put the card back
        if communityCard != 6:  # except GOOJF card
            board.communityCards.append(communityCard)
