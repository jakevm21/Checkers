from game_settings import GameSettings
from piece_options import PieceOptions as po


class Game:
    def __init__(self) -> None:
        self.prefs = self._match_settings()

    def _match_settings(self) -> GameSettings:
        # Get num players
        num_players = self._num_players()

        # Get player colors
        if num_players == 1:
            p1 = self._player_color()
            p2 = po.red if p1 == po.blk else po.blk
        else:
            p1 = po.red
            p2 = po.blk
        
        return GameSettings(num_players, p1, p2)

    def _num_players(self) -> int:
        SINGLE_PLAYER = ("1", "one")
        MULTI_PLAYER = ("2", "two")

        while True:
            ch = input("How many players?\n" 
                       "1 -- One player\n"
                       "2 -- Two players\n"
                       "> ").lower().strip()
            # Player vs ai
            if ch in SINGLE_PLAYER:
                return 1
            # 2 human players
            elif ch in MULTI_PLAYER:
                return 2
            else:
                print("Invalid selection...")

    def _player_color(self) -> str:
        BLACK = ("1", "black")
        RED = ("2", "red")

        while True:
            ch = input("What color would you like to play as?\n"
                       "1 -- Black\n"
                       "2 -- Red\n"
                       "> ").lower().strip()
            if ch in BLACK:
                return po.blk
            elif ch in RED:
                return po.red
            else:
                print("Invalid selection...")

