import random
from config import Config

class Snake():
    UP = 'up'
    RIGHT = 'right'
    LEFT = 'left'
    DOWN = 'down'
    HEAD = 0
    Directions = ["up","right","left","down"]
    def __init__(self):
        self.x = random.randint(5,Config.CELLWIDTH- 6)
        self.y = random.randint(5,Config.CELLHEIGHT - 6)
        self.direction = self.RIGHT
        self.wormCoords = [{'x': self.x , 'y':self.y},
                           {'x': self.x-1, 'y': self.y},
                           {'x': self.x-2, 'y': self.y},]

    def update(self,apple):
        if self.wormCoords[self.HEAD]['x'] == apple.x and self.wormCoords[self.HEAD]['y'] == apple.y :
            apple.setNewlocation()
        else:
            del self.wormCoords[-1]

        if self.direction == self.RIGHT:
            newHead = {'x': self.wormCoords[self.HEAD]
                            ['x'] + 1, 'y': self.wormCoords[self.HEAD]['y']}

        elif self.direction == self.LEFT:
            newHead = {'x': self.wormCoords[self.HEAD]
                            ['x'] - 1, 'y': self.wormCoords[self.HEAD]['y']}
        elif self.direction == self.UP:
            newHead = {'x': self.wormCoords[self.HEAD]
            ['x'], 'y': self.wormCoords[self.HEAD]['y'] - 1}
        elif self.direction == self.DOWN:
            newHead = {'x': self.wormCoords[self.HEAD]
            ['x'], 'y': self.wormCoords[self.HEAD]['y'] + 1}

        self.wormCoords.insert(0, newHead)

