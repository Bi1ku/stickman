from classes.moveable import Moveable
from utils import load_asset


class Lazer(Moveable):
    def __init__(self, pos, direction):
        self.image = load_asset("assets/lazer/lazer.png")
        super().__init__(self.image, pos, 10, direction)

    def update(self):
        self.move()
        self.destroy()
