class Cell:
    """Generic Cell Class, base for other classes"""

    def __init__(self, name):
        self.name = name
        self.group = ""

    def action(self, player):
        pass
