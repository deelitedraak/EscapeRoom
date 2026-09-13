from EscapeRoom import EscapeRoom


class Spelsessie:
    def __init__(self, teamnaam, escape_room: EscapeRoom):
        self.teamnaam = teamnaam
        self.escape_room = escape_room
        self.huidige_puzzel_index = 0
        self.score = 0
        self.gebruikte_hints = []

        for puzzel in self.escape_room.get_puzzels():
            self.gebruikte_hints.append(0)


    def get_huidige_puzzel(self):
        return self.escape_room.get_puzzels()[self.huidige_puzzel_index]

    def vraag_hint(self):
        puzzel = self.get_huidige_puzzel()
        aantal_gebruikte_hints = self.gebruikte_hints[self.huidige_puzzel_index]
        hint = puzzel.get_hint(aantal_gebruikte_hints)

        if hint is not None:
            self.gebruikte_hints[self.huidige_puzzel_index] += 1
            return hint
        else:
            return None

    def geef_antwoord(self, antwoord):
        puzzel = self.get_huidige_puzzel()

        if puzzel.controleer_oplossing(antwoord):
            aantal_gebruikte_hints = self.gebruikte_hints[self.huidige_puzzel_index]
            punten = puzzel.bereken_punten(aantal_gebruikte_hints)
            self.score += punten
            self.huidige_puzzel_index += 1
            return True

        else:
            return False

    def is_afgerond(self):
        return self.huidige_puzzel_index >= len(self.escape_room.get_puzzels())

    def get_voortgang(self):
        aantal_puzzels = len(self.escape_room.get_puzzels())
        return self.huidige_puzzel_index / aantal_puzzels * 100


