from Hint import Hint
from Spelsessie import Spelsessie

class Puzzel:
    def __init__(self, titel, opdracht, oplossing, max_punten):
        self.titel = titel
        self.opdracht = opdracht
        self.oplossing = oplossing
        self.max_punten = max_punten
        self.hint_lijst = []

    def voeg_hint_toe(self, hint:Hint):
        self.hint_lijst.append(hint)

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

    def controleer_oplossing(self, antwoord):
        return antwoord.upper() == self.oplossing.upper()

    def bereken_punten(self, aantal_gebruikte_hints):
        punten = self.max_punten

        for hint in self.hint_lijst[:aantal_gebruikte_hints]:
            punten -= hint.get_strafpunten()

        return max(0, punten)

    def get_hint(self, index):
        if 0 <= index < len(self.hint_lijst):
            return self.hint_lijst[index]
        return None
        