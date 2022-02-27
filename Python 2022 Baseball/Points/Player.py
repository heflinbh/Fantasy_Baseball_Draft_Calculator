class Player:

    def __init__(self, name, points, position):
        self.name = name
        self.positions = [position]
        self.points = points

    def addPosition(self, pos):
        self.positions.append(pos)

    def equals(self, other):
        return self.name == other.name and self.points == other.points and self.positions == other.positions

