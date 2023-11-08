class IteratorTeam:
    def __init__(self):
        self.team = Team()
        self.i = 0

    def __next__(self):
        if x < len(self.team.juniors):
            x = self.i
            self.i += 1
            return self.team.juniors[x]
        else:
            raise StopIteration


class Team:
    def __init__(self):
        self.juniors = ["JPlayer 1", "JPlayer 2", "JPlayer 3", "JPlayer 4", "JPlayer 5"]
        self.seniors = ["Player 1", "Player 2", "Player 3"]

    def __iter__(self):
        return IteratorTeam


for x in Team():
    print(x)
