import sqlite3
from EscapeRoom import EscapeRoom
from Puzzel import Puzzel
from Hint import Hint
from ScoreResultaat import ScoreResultaat

class Database:
    def __init__(self, bestandsnaam):
        self.bestandsnaam = bestandsnaam

    def initialiseer(self):
        verbinding = sqlite3.connect(self.bestandsnaam)
        verbinding.execute("PRAGMA foreign_keys = ON")

        cursor = verbinding.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS escape_room (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                naam TEXT NOT NULL,
                thema TEXT NOT NULL,
                tijdslimiet INTEGER NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS puzzel (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                room_id INTEGER NOT NULL,
                titel TEXT NOT NULL,
                opdracht TEXT NOT NULL,
                oplossing TEXT NOT NULL,
                max_punten INTEGER NOT NULL,
                volgorde INTEGER NOT NULL,
                FOREIGN KEY (room_id) REFERENCES escape_room(id)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hint (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                puzzel_id INTEGER NOT NULL,
                tekst TEXT NOT NULL,
                strafpunten INTEGER NOT NULL,
                volgorde INTEGER NOT NULL,
                FOREIGN KEY (puzzel_id) REFERENCES puzzel(id)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS score_resultaat (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                room_id INTEGER NOT NULL,
                teamnaam TEXT NOT NULL,
                score INTEGER NOT NULL,
                FOREIGN KEY (room_id) REFERENCES escape_room(id)
            )
        """)

        verbinding.commit()
        verbinding.close()


    def room_bestaat(self, roomnaam):
        verbinding = sqlite3.connect(self.bestandsnaam)
        cursor = verbinding.cursor()

        cursor.execute("""
            SELECT id
            FROM escape_room
            WHERE naam = ?  COLLATE NOCASE
            LIMIT 1
        """, (roomnaam,))

        room_rij = cursor.fetchone()

        verbinding.close()

        return room_rij is not None

    def sla_room_op(self, room):
        verbinding = sqlite3.connect(self.bestandsnaam)
        verbinding.execute("PRAGMA foreign_keys = ON")

        cursor = verbinding.cursor()
        cursor.execute("""
            INSERT INTO escape_room (naam, thema, tijdslimiet)
            VALUES (?, ?, ?)
        """, (
            room.get_naam(),
            room.thema,
            room.tijdslimiet
        ))

        room_id = cursor.lastrowid

        for volgorde_puzzel, puzzel in enumerate(room.get_puzzels()):
            cursor.execute("""
                INSERT INTO puzzel (
                    room_id,
                    titel,
                    opdracht,
                    oplossing,
                    max_punten,
                    volgorde
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                room_id,
                puzzel.titel,
                puzzel.opdracht,
                puzzel.oplossing,
                puzzel.max_punten,
                volgorde_puzzel
            ))

            puzzel_id = cursor.lastrowid

            for volgorde_hint, hint in enumerate(puzzel.hint_lijst):
                cursor.execute("""
                    INSERT INTO hint (
                        puzzel_id,
                        tekst,
                        strafpunten,
                        volgorde
                    )
                    VALUES (?, ?, ?, ?)
                """, (
                    puzzel_id,
                    hint.tekst,
                    hint.strafpunten,
                    volgorde_hint
                ))

        verbinding.commit()
        verbinding.close()

        return room_id

    def laad_rooms(self):
        verbinding = sqlite3.connect(self.bestandsnaam)
        verbinding.execute("PRAGMA foreign_keys = ON")

        cursor = verbinding.cursor()

        rooms = []

        cursor.execute("""
            SELECT id, naam, thema, tijdslimiet
            FROM escape_room
            ORDER BY id
        """)

        room_rijen = cursor.fetchall()

        for room_id, naam, thema, tijdslimiet in room_rijen:
            room = EscapeRoom(naam, thema, tijdslimiet)

            cursor.execute("""
                SELECT id, titel, opdracht, oplossing, max_punten
                FROM puzzel
                WHERE room_id = ?
                ORDER BY volgorde
            """, (room_id,))

            puzzel_rijen = cursor.fetchall()

            for puzzel_id, titel, opdracht, oplossing, max_punten in puzzel_rijen:
                puzzel = Puzzel(
                    titel,
                    opdracht,
                    oplossing,
                    max_punten
                )

                cursor.execute("""
                    SELECT tekst, strafpunten
                    FROM hint
                    WHERE puzzel_id = ?
                    ORDER BY volgorde
                """, (puzzel_id,))

                hint_rijen = cursor.fetchall()

                for tekst, strafpunten in hint_rijen:
                    hint = Hint(tekst, strafpunten)
                    puzzel.voeg_hint_toe(hint)

                room.voeg_puzzel_toe(puzzel)

            rooms.append(room)

        verbinding.close()

        return rooms

    def sla_score_op(self, resultaat):
        verbinding = sqlite3.connect(self.bestandsnaam)
        verbinding.execute("PRAGMA foreign_keys = ON")
        cursor = verbinding.cursor()

        cursor.execute("""
            SELECT id
            FROM escape_room
            WHERE naam = ?
            LIMIT 1
        """, (resultaat.roomnaam,))

        room_rij = cursor.fetchone()

        if room_rij is None:
            verbinding.close()
            return False

        room_id = room_rij[0]

        cursor.execute("""
            INSERT INTO score_resultaat (
                room_id,
                teamnaam,
                score
            )
            VALUES (?, ?, ?)
        """, (
            room_id,
            resultaat.teamnaam,
            resultaat.score
        ))

        verbinding.commit()
        verbinding.close()

        return True

    def laad_scorebord(self):
        verbinding = sqlite3.connect(self.bestandsnaam)
        cursor = verbinding.cursor()

        cursor.execute("""
            SELECT
                score_resultaat.teamnaam,
                escape_room.naam,
                score_resultaat.score
            FROM score_resultaat
            JOIN escape_room
                ON score_resultaat.room_id = escape_room.id
        """)

        rijen = cursor.fetchall()

        scorebord = []

        for teamnaam, roomnaam, score in rijen:
            resultaat = ScoreResultaat(
                teamnaam,
                roomnaam,
                score
            )
            scorebord.append(resultaat)

        verbinding.close()

        return scorebord


if __name__ == "__main__":
    database = Database("escaperoom.db")
    database.initialiseer()



