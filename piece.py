class Piece:
    def __init__(self, surface, pos, color, mass, name, transition=False):
        self.x, self.y = pos
        self.mass = mass
        self.splitting = transition
        self.surface = surface
        self.name = name

    def draw(self):
        pass

    def update(self):
        if self.splitting:
            pass
