class Car:
    def __init__(self, name, year, player):
        self.name = name
        self.year = year
        self.player = player

    def get_info(self):
        return f"{self.player} владеет машинй {self.name} {self.year} года выпуска."