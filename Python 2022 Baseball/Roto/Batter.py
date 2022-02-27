class Batter:

    def __init__(self, name, position, hits, atBats, homeRuns, rbi, stolenBases, runs):
        self.name = name
        self.positions = [position]
        self.hits = hits
        self.atBats = atBats
        self.homeRuns = homeRuns
        self.rbi = rbi
        self.stolenBases = stolenBases
        self.runs = runs

        self.average_helper = self.atBats - self.hits


    def addPosition(self, pos):
        self.positions.append(pos)

    

