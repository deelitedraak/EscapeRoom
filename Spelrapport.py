from reportlab.pdfgen import canvas


class Spelrapport:
    def __init__(self, spelsessie):
        self.spelsessie = spelsessie

    def genereer_pdf(self, bestandsnaam):
        pdf = canvas.Canvas(bestandsnaam)

        pdf.drawString(50, 750, f"Team: {self.spelsessie.teamnaam}")
        pdf.drawString(50, 730,f"Escape room: {self.spelsessie.escape_room.get_naam()}")
        pdf.drawString(50, 710, f"Eindscore: {self.spelsessie.score}")

        y = 670

        for index, puzzel in enumerate(self.spelsessie.escape_room.get_puzzels()):
            aantal_hints = self.spelsessie.gebruikte_hints[index]

            pdf.drawString(50, y, f"Puzzel: {puzzel.get_titel()}")
            y -= 20

            pdf.drawString(70, y, f"Gebruikte hints: {aantal_hints}")
            y -= 30

        pdf.save()