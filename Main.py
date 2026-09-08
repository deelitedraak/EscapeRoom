from Escaperoom import EscapeRoom
from Puzzel import Puzzel
from Hint import Hint


def main():


    room1 = EscapeRoom("De Verloren Tempel", "Avontuur", 60)
    puzzel1 = Puzzel("De Schatkaart", "Vind de schat door de aanwijzingen te volgen.", "Schat", 10)
    hint1 = Hint("Kijk goed naar de symbolen op de kaart.", 2)

    puzzel1.voeg_hint_toe(hint1)
    room1.voeg_puzzel_toe(puzzel1)

    rooms = [room1]
    gekozen_room = rooms[keuze - 1]
    keuze = input(int("Kies een room: "))
    print(gekozen_room)

    for nummer, room in enumerate(rooms, start=1):
        print(f"{nummer}. {room.get_naam()}")

if __name__ == "__main__":
    main()