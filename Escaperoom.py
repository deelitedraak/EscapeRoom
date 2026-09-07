import Puzzel


class Escaperoom:
    def __init__(self, naam, thema, tijdslimiet):
        self.naam = naam
        self.thema = thema
        self.tijdslimiet = tijdslimiet
        self.puzzels = []

    def voeg_puzzel_toe(self, puzzel:Puzzel):
        self.puzzels.append(puzzel)

    def get_puzzels(self):
        return self.puzzels

    def get_naam(self):
        return self.naam