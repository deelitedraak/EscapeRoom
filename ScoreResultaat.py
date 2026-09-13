
class ScoreResultaat:
    def __init__(self, teamnaam, roomnaam, score):
        self.teamnaam = teamnaam
        self.roomnaam = roomnaam
        self.score = score

    def __str__(self):
        return(
            f"Team: {self.teamnaam} | Room: {self.roomnaam} | Score: {self.score}"
        )


