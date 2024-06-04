from classes.moveable import Moveable
from utils import load_asset


class Tile(Moveable):
    def __init__(self, pos, direction):
        super().__init__(load_asset("assets/tile/tile.png"), pos, direction)

    def update(self):
        super().move()
