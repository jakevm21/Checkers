from game_settings import GameSettings
from gamestate import GameState
from gui import GUI
from piece_options import PieceOptions as po
BLK_PIECES = (po.blk_r, po.blk_k)
RED_PIECES = (po.red_r, po.red_k)


class Game:
    def __init__(self) -> None:
        self.prefs = self._match_settings()
        self.gs = GameState()
        self.gui = self._gui_setup()

    def _match_settings(self) -> GameSettings:
        # Get num players
        num_players = self._num_players()

        # Get player colors
        if num_players == 1:
            p1 = self._choose_player_color()
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
                print("\nInvalid selection...\n")

    def _choose_player_color(self) -> str:
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
                print("\nInvalid selection...\n")

    def _draw_board(self) -> None:
        pass

    def _gui_setup(self) -> GUI:
        gui = GUI()
        for i, row in enumerate(self.gs.get_board()):
            for j, sq in enumerate(row):
                if sq != po.empty:
                    if sq == po.blk_r or sq == po.blk_k:
                        color = po.blk
                    else:
                        color = po.red
                    if sq == po.blk_r or sq == po.red_r:
                        rank = po.reg
                    else:
                        rank = po.kng
                    gui.draw_checker(i, j, color, rank)
        return gui

    def _draw_checkers(self):
        for row in range(len(self.gs.get_board())):
            for col in range(len(self.gs.get_board()[0])):
                if self.gs.get_board[row][col] in BLK_PIECES or\
                   self.gs.get_board[row][col] in RED_PIECES:
                   pass
