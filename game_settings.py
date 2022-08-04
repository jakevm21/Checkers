from constants import *

class GameSettings:
    def __init__(self, num_plrs: int, p1_color=BLK, p2_color=RED) -> None:
        self._num_plrs = num_plrs
        self._p1_color = p1_color
        self._p2_color = p2_color

    def get_num_players(self) -> int:
        return self._num_plrs
    
    def get_p1_color(self) -> str:
        return self._p1_color
    
    def get_p2_color(self) -> str:
        return self._p2_color
