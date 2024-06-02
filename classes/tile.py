from classes.entity import Entity
from utils import load_asset


class Tile(Entity):
    def __init__(self, pos):
        super().__init__(load_asset("assets/tile/tile.png"), pos)
