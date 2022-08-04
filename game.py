import turtle as turt
from typing import List, Tuple
from game_settings import GameSettings
from gamestate import GameState
from gui import GUI
from constants import *
from pieces import *


class Game:
    def __init__(self) -> None:
        self._prefs = self._match_settings()
        self._gs = GameState()
        self._gui = self._gui_setup()
        self._screen = turt.Screen()
        self._game_loop()

    def _match_settings(self) -> GameSettings:
        # Get num players
        num_players = self._num_players()

        # Get player colors
        if num_players == 1:
            p1 = self._choose_player_color()
            p2 = RED if p1 == BLK else BLK
        else:
            p1 = RED
            p2 = BLK
        
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
        OPT_1 = ("1", "black")
        OPT_2 = ("2", "red")

        while True:
            ch = input("What color would you like to play as?\n"
                       "1 -- Black\n"
                       "2 -- Red\n"
                       "> ").lower().strip()
            if ch in OPT_1:
                return BLK
            elif ch in OPT_2:
                return RED
            else:
                print("\nInvalid selection...\n")

    def _gui_setup(self) -> GUI:
        gui = GUI()
        gui.draw_board(self._gs.get_board())
        return gui

    def _is_inbounds(self, x: float, y: float) -> bool:
        return x < self._gui.get_x_max() and y < self._gui.get_y_max() and \
               x > self._gui.get_x_min() and y > self._gui.get_y_min()

    def _is_player_piece(self, row: int, col: int) -> bool:
        sq = self._gs.get_board()[row][col]
        return sq and sq.get_color() == self._gs.get_cur_player()

    def _get_available_moves(self, row: int, col: int) -> List[Tuple[int, int]]:
        moves = []
        piece = self._gs.get_board()[row][col]

        for sq in piece.get_moves(row, col, self._gs.get_board()):
            moves.append(sq)

        return moves

    def _handle_move(self, row: int, col: int) -> None:
        if (row, col) not in self._gs.get_selected_piece_moves():
            print("That is not a valid move!")
            return
        else:
            self._gs.move_piece(row, col)
            self._gui.draw_board(self._gs.get_board())
            self._gs.swap_turn()

    def _click_handler(self, x: float, y: float) -> None:
        print("Clicked at", x, y)

        if not self._is_inbounds(x, y):
            print("Click was out of bounds!")
            return
        
        row, col = self._gui.click_to_square(x, y)

        if self._gs.selection_made():
            self._handle_move(row, col)
        else:
            if not self._is_player_piece(row, col):
                print("That's not your piece!")
                return
            else:
                print("That's your piece!")

            moves = self._get_available_moves(row, col)
            if not moves:
                print("That piece cannot move!")
                return
            else:
                print("That piece can move!")
                print(moves)
                # update gamestate
                self._gs.select_piece(row, col, moves)
                # update gui
                self._gui.clear_board()
                self._gui.draw_board(self._gs.get_board())
                self._gui.select_piece(row,
                                      col,
                                      self._gs.get_board()[row][col],
                                      self._gs.get_selected_piece_moves())

        if self._gs.game_over():
            self._gui.victory_msg(self._gs.get_winner())

    def _game_loop(self):
        self._gui.draw_board(self._gs.get_board())
        self._screen.onclick(self._click_handler)

        turt.done()
