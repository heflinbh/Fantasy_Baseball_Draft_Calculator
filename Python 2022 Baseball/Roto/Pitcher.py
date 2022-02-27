from matplotlib.pyplot import hist
from numpy import histogram_bin_edges


class Pitcher:

    def __init__(self, name, position, runs, inningsPitched, wins, hits, walks, strikeouts, saves):
        self.name = name
        self.positions = [position]
        self.runs = runs
        self.inningsPitched = inningsPitched
        self.wins = wins
        self.hits = hits
        self.walks = walks
        self.strikeouts = strikeouts
        self.saves = saves

        self.era_helper = self.inningsPitched - self.runs
        self.whip_helper = self.inningsPitched - self.hits - self.walks


    def addPosition(self, pos):
        self.positions.append(pos)

    