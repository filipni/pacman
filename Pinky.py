from consts import *
from Ghost import *

class Pinky(Ghost):

    def __init__(self, pos):
        super().__init__('Pinky', PINK, pos, (0, 1))

    def ChaseUpdate(self, entities):
        assert 'Pac' in entities, 'Pacman must be in the dictionary'

        pac = entities['Pac']
        y = pac.pos[0]
        x = pac.pos[1]

        if pac.direction == UP:
            y -= 4
            x -= 4
        elif pac.direction == DOWN:
            y += 4
        elif pac.direction == LEFT:
            x -= 4
        else:
            x += 4

        return self.CheckPosBounds((y,x))
