from EscapeRoom import EscapeRoom
from Puzzel import Puzzel
from Hint import Hint
from Spelsessie import Spelsessie
from ScoreResultaat import ScoreResultaat


def main():

    scorebord = []
   
    # Room 1 - De Verloren Tempel
    room1 = EscapeRoom("De Verloren Tempel", "Archeologie en avontuur", 60)

    puzzel1 = Puzzel(
        "De Zonneschijf",
        "Op een stenen schijf staat: Zon = 3, Maan = 5, Ster = 2. "
        "Daaronder staat: (Zon x Maan) + Ster. Welk getal opent het slot?",
        "17",
        10
    )

    puzzel2 = Puzzel(
        "Het Raadsel van de Sfinx",
        "Wat loopt in de ochtend op vier benen, in de middag op twee "
        "en in de avond op drie?",
        "mens",
        15
    )

    puzzel3 = Puzzel(
        "De Vier Wachters",
        "Vier beelden dragen een cijfer en een letter: "
        "Muis D, Baviaan U, Olifant R, Valk E. "
        "Wanneer de letters in de juiste volgorde staan kan je dit woord openen"
        "Welk woord vormt de sleutel?",
        "DEUR",
        10
    )

    hint1 = Hint(
        "Vermenigvuldig eerst de waarden van de zon en maan.",
        2
    )

    hint2 = Hint(
        "De ochtend, middag en avond stellen levensfasen voor.",
        3
    )

    hint3 = Hint(
        "Sorteer de wachters op hun grootte en lees daarna de letters.",
        2
    )

    puzzel1.voeg_hint_toe(hint1)
    puzzel2.voeg_hint_toe(hint2)
    puzzel3.voeg_hint_toe(hint3)

    room1.voeg_puzzel_toe(puzzel1)
    room1.voeg_puzzel_toe(puzzel2)
    room1.voeg_puzzel_toe(puzzel3)


    # Room 2 - Noodtoestand op de Nautilus
    room2 = EscapeRoom("Noodtoestand op de Nautilus", "Onderzeeër en techniek", 50)

    puzzel4 = Puzzel(
        "De Drukregelaar",
        "Drie drukmeters tonen A = 8, B = 3 en C = 5. "
        "Op het bedieningspaneel staat: A + C - B. "
        "Welke waarde moet je instellen?",
        "10",
        10
    )

    puzzel5 = Puzzel(
        "Het Noodsignaal",
        "De radio ontvangt steeds hetzelfde bericht: ... --- ... "
        "Welk internationaal noodsignaal wordt hier verzonden?",
        "SOS",
        15
    )

    puzzel6 = Puzzel(
        "Het Vergrendelde Periscoop",
        "Op een beschadigd bedieningspaneel staat: "
        "16-5-18-9-19-3-15-15-16. "
        "Iedere letter van het alfabet heeft een nummer waarbij A=1, B=2 enzovoort. "
        "Welk woord vormt de code?",
        "PERISCOOP",
        20
    )

    hint4 = Hint(
        "Vul eerst de drie waarden in de formule in.",
        2
    )

    hint5 = Hint(
        "Het bericht is geschreven in morsecode.",
        3
    )

    hint6 = Hint(
        "Zet ieder getal om naar de bijbehorende letter van het alfabet.",
        4
    )

    puzzel4.voeg_hint_toe(hint4)
    puzzel5.voeg_hint_toe(hint5)
    puzzel6.voeg_hint_toe(hint6)

    room2.voeg_puzzel_toe(puzzel4)
    room2.voeg_puzzel_toe(puzzel5)
    room2.voeg_puzzel_toe(puzzel6)


    # Room 3 - Het Verlaten Ruimtestation
    room3 = EscapeRoom("Het Verlaten Ruimtestation", "Sciencefiction en ruimtevaart", 55)

    puzzel7 = Puzzel(
        "Zuurstofprotocol",
        "Het zuurstofsysteem vraagt om de volgende waarde in de reeks: "
        "2, 4, 8, 16, ?. Welke waarde moet worden ingevoerd?",
        "32",
        10
    )

    puzzel8 = Puzzel(
        "Het Versleutelde Logboek",
        "In het logboek staat het woord SODQHHW. "
        "De boordcomputer vermeldt: Caesar-versleuteling, verschuiving +3. "
        "Welk oorspronkelijk woord werd verstuurd?",
        "PLANEET",
        20
    )

    puzzel9 = Puzzel(
        "Navigatiecomputer",
        "Ik ben de zesde planeet vanaf de zon, heb een opvallend ringenstelsel "
        "en ben na Jupiter de grootste planeet van het zonnestelsel. "
        "Welke planeet ben ik?",
        "SATURNUS",
        15
    )

    hint7 = Hint(
        "Iedere waarde is twee keer zo groot als de vorige.",
        2
    )

    hint8 = Hint(
        "Verschuif iedere letter drie plaatsen terug in het alfabet.",
        4
    )

    hint9 = Hint(
        "Denk aan de planeet die vooral bekendstaat om zijn ringen.",
        3
    )

    puzzel7.voeg_hint_toe(hint7)
    puzzel8.voeg_hint_toe(hint8)
    puzzel9.voeg_hint_toe(hint9)

    room3.voeg_puzzel_toe(puzzel7)
    room3.voeg_puzzel_toe(puzzel8)
    room3.voeg_puzzel_toe(puzzel9)


    rooms = [room1, room2, room3]

    while True:
        print("1. Escape room ontwerpen")
        print("2. Escape room spelen")
        print("3. Scorebord bekijken")
        print("4. Afsluiten")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            print("Ontwerpmodus")
            while True:
                naam = input("Naam van de escape room: ")

                if naam.strip() == "":
                    print("Titel mag niet leeg zijn.")
                else:
                    break

            while True:
                thema = input("Thema van de escape room: ")

                if thema.strip() == "":
                    print("Thema mag niet leeg zijn.")
                else:
                    break

            while True:
                try:
                    tijdslimiet = int(input("Tijdslimiet van de escaperoom: "))

                    if tijdslimiet > 0:
                        break
                    else:
                        print("Tijdslimiet moet groter zijn dan 0.")

                except ValueError:
                    print("Voer een geldig geheel getal in.")

            nieuwe_room = EscapeRoom(naam, thema, tijdslimiet)

            while True:

                while True:
                    titel = input("Titel van de puzzel: ")

                    titel_bestaat = False

                    for puzzel in nieuwe_room.get_puzzels():
                        if puzzel.get_titel().lower() == titel.lower():
                            titel_bestaat = True

                    if titel.strip() == "":
                        print("Titel mag niet leeg zijn.")
                    elif titel_bestaat:
                        print("Deze puzzeltitel bestaat al.")
                    else:
                        break

                opdracht = input("Opdracht van de puzzel: ")
                oplossing = input("Oplossing van de puzzel: ")

                while True:
                    try:
                        max_punten = int(input("Maximale punten van de puzzel: "))

                        if max_punten > 0:
                            break
                        else:
                            print("Maximale punten moet groter zijn dan 0")
                    except ValueError:
                        print("Voer een geldig heel getal in.")

                nieuwe_puzzel = Puzzel(titel, opdracht, oplossing, max_punten)

                while True:
                    while True:
                        hint_tekst = input("Tekst van de hint: ")

                        if hint_tekst.strip() == "":
                            print("Tekst mag niet leeg zijn")
                        else:
                            break

                    while True:
                        try:
                            strafpunten = int(input("Strafpunten van de hint: "))

                            if 0 <= strafpunten <= max_punten:
                                break
                            else:
                                print("Strafpunten moeten tussen 0 en de maximale punten liggen.")
                        except ValueError:
                            print("Voer een geldig geheel getal in.")

                    nieuwe_hint = Hint(hint_tekst, strafpunten)
                    nieuwe_puzzel.voeg_hint_toe(nieuwe_hint)

                    while True:
                        nog_een_hint = input("Nog een hint toevoegen? (j/n): ").lower()

                        if nog_een_hint == "j" or nog_een_hint == "n":
                            break
                        else:
                            print("Kies j of n.")

                    if nog_een_hint == "n":
                        break
                nieuwe_room.voeg_puzzel_toe(nieuwe_puzzel)
                if len(nieuwe_room.get_puzzels()) < 2:
                    print("Een escape room moet minimaal 2 puzzels bevatten.")
                    continue
                while True:
                    nog_een_puzzel = input("Nog een puzzel toevoegen? (j/n): ").lower()

                    if nog_een_puzzel == "j" or nog_een_puzzel == "n":
                        break
                    else:
                        print("Kies j of n.")

                if nog_een_puzzel == "n":
                    break
            rooms.append(nieuwe_room)

        elif keuze == "2":
            for nummer, room in enumerate(rooms, start=1):
                print(f"{nummer}. {room.get_naam()}")

            while True:
                keuze = int(input("Kies een room: "))
                if not 1 <= keuze <= len(rooms):
                    print("Escape room niet gevonden.")
                else:
                    gekozen_room = rooms[keuze - 1]
                    break

            print(f"Je hebt gekozen voor: {gekozen_room.get_naam()}")

            teamnaam = input("bedenk een teamnaam: ")
            spelsessie = Spelsessie(teamnaam, gekozen_room)

            while not spelsessie.is_afgerond():
                puzzel = spelsessie.get_huidige_puzzel()
                print(puzzel)

                print("1. antwoord geven")
                print("2. Hint vragen")

                actie = input("Kies actie 1 of 2: ")
                if actie == "1":
                    antwoord = input("Wat is je antwoord: ")
                    correct = spelsessie.geef_antwoord(antwoord)
                    if correct:
                        print("Correct!")
                    else:
                        print("Helaas, probeer het opnieuw.")
                elif actie == "2":
                    hint = spelsessie.vraag_hint()
                    if hint is not None:
                        print(hint)
                    else:
                        print("Er zijn geen hints meer beschikbaar")
                else:
                    print("Ongeldige keuze. Kies 1 of 2.")

                print(f"Score {spelsessie.score}")
                print(f"Voortgang {spelsessie.get_voortgang():.1f}%")
                
            print("Gefeliciteerd! Je bent uit de escape room ontsnapt.")
            print(f"Score {spelsessie.score}")
            print(f"Voortgang {spelsessie.get_voortgang():.1f}%")

            resultaat = ScoreResultaat(
                spelsessie.teamnaam,
                gekozen_room.get_naam(),
                spelsessie.score
                )
            
            scorebord.append(resultaat)

        elif keuze == "3":

            
            if len(scorebord) == 0:
                print("Er zijn nog geen scores")
            else:
                gesorteerd_scorebord = sorted(
                    scorebord,
                    key=lambda resultaat: (-resultaat.score, resultaat.teamnaam.lower())
                )
                
                for resultaat in gesorteerd_scorebord:
                    print(resultaat)


        elif keuze == "4":
            break

        else:
            print("Ongeldige keuze.")


    


if __name__ == "__main__":
    main()
