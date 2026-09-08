from Puzzel import Puzzel


class EscapeRoom:
    def __init__(self, naam, thema, tijdslimiet):
        self.naam = naam
        self.thema = thema
        self.tijdslimiet = tijdslimiet
        self.puzzel_lijst = []

    def voeg_puzzel_toe(self, puzzel:Puzzel):
        self.puzzel_lijst.append(puzzel)

    def get_puzzels(self):
        return self.puzzel_lijst

    def get_naam(self):
        return self.naam

    def __str__(self):

        puzzel_info_lijst = []

        for nummer, puzzel in enumerate(self.puzzel_lijst, start=1):
            puzzel_info = f"Puzzel {nummer}:\n{puzzel}\n"
            puzzel_info_lijst.append(puzzel_info)

        room_puzzels = "\n".join(puzzel_info_lijst)

        return (
            f"Naam: {self.naam}\n"
            f"Thema: {self.thema}\n"
            f"Tijdslimiet: {self.tijdslimiet}\n"
            f"Puzzels:\n{room_puzzels}"
        )