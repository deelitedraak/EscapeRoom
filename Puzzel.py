from Hint import Hint


class Puzzel:
    def __init__(self, titel, opdracht, oplossing, max_punten):
        self.titel = titel
        self.opdracht = opdracht
        self.oplossing = oplossing
        self.max_punten = max_punten
        self.hints = []

    def voeg_hint_toe(self, hint:Hint):
        self.hints.append(hint)

    def get_titel(self):
        return self.titel

    def get_max_punten(self):
        return self.max_punten

    def __str__(self):
        return (
            f"Titel: {self.titel}\n"
            f"Opdracht: {self.opdracht}\n"
            f"Maximale punten: {self.max_punten}\n"
        )