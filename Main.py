from EscapeRoom import EscapeRoom
from Puzzel import Puzzel
from Hint import Hint


def main():

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
        "Jakhals 1=D, Baviaan 2=E, Valk 3=U, Mens 4=R. "
        "Zet de letters in de volgorde 1 tot en met 4. "
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
        "Sorteer de wachters op hun nummer en lees daarna de letters.",
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

    for nummer, room in enumerate(rooms, start=1):
        print(f"{nummer}. {room.get_naam()}")

    keuze = int(input("Kies een room: "))
    gekozen_room = rooms[keuze - 1]

    print(gekozen_room)


if __name__ == "__main__":
    main()