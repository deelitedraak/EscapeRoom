class Hint:
    def __init__(self, tekst, strafpunten):
        self.tekst = tekst
        self.strafpunten = strafpunten

    def get_strafpunten(self):
        return self.strafpunten

    def __str__(self):
        return (
            f"Hint: {self.tekst}\n"
            f"Strafpunten: {self.strafpunten}\n"
        )