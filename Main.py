from EscapeRoom import EscapeRoom
from Puzzel import Puzzel
from Hint import Hint


def main():


    room1 = EscapeRoom("De Verloren Tempel", "Avontuur", 60)
    puzzel1 = Puzzel("De Schatkaart", "Vind de schat door de aanwijzingen te volgen.", "Schat", 10)
    hint1 = Hint("Kijk goed naar de symbolen op de kaart.", 2)

    puzzel1.voeg_hint_toe(hint1)
    room1.voeg_puzzel_toe(puzzel1)

    for nummer, room in enumerate(rooms, start=1):
        print(f"{nummer}. {room.get_naam()}")

    rooms = [room1]
    keuze = int(input("Kies een room: "))
    gekozen_room = rooms[keuze - 1]
    print(gekozen_room)

if __name__ == "__main__":
    main()