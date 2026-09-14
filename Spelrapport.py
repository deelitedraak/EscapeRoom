from reportlab.pdfgen import canvas


class Spelrapport:
    def __init__(self, spelsessie):
        self.spelsessie = spelsessie

    def genereer_pdf(self, bestandsnaam):
        pdf = canvas.Canvas(bestandsnaam)
        pdf.setTitle("Escape Room Spelrapport")

        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(50, 800, "Escape Room Spelrapport")

        pdf.setFont("Helvetica", 11)
        pdf.drawString(50, 770, f"Team: {self.spelsessie.teamnaam}")
        pdf.drawString(50, 750, f"Escape room: {self.spelsessie.escape_room.get_naam()}")
        pdf.drawString(50, 730, f"Eindscore: {self.spelsessie.score}")

        y = 690

        for index, puzzel in enumerate(self.spelsessie.escape_room.get_puzzels()):
            aantal_hints = self.spelsessie.gebruikte_hints[index]

            pdf.setFont("Helvetica-Bold", 11)
            pdf.drawString(50, y, f"Puzzel: {puzzel.get_titel()}")
            y -= 20

            pdf.setFont("Helvetica", 10)

            if aantal_hints == 0:
                pdf.drawString(70, y, "Gebruikte hints: geen")
                y -= 30
            else:
                pdf.drawString(70, y, "Gebruikte hints:")
                y -= 18

                for hint in puzzel.hint_lijst[:aantal_hints]:
                    pdf.drawString(
                        90,
                        y,
                        f"- {hint.tekst} (-{hint.strafpunten} punten)"
                    )
                    y -= 18

                y -= 12

        pdf.save()
