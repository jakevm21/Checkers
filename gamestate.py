'''
Jake Van Meter
CS5001 Fall 2021
Gamestate class. Handles the logic regarding whose turn it is, whether there
is an ai player or two human players, and whether the game over conditions
have been met.
'''
from typing import Set, Tuple
from piece_options import *
from pieces import *
DEFAULT_BOARD = [
    [None, BlackPiece(), None, BlackPiece(), None, BlackPiece(), None, BlackPiece()],
    [BlackPiece(), None, BlackPiece(), None, BlackPiece(), None, BlackPiece(), None],
    [None, BlackPiece(), None, BlackPiece(), None, BlackPiece(), None, BlackPiece()],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [RedPiece(), None, RedPiece(), None, RedPiece(), None, RedPiece(), None],
    [None, RedPiece(), None, RedPiece(), None, RedPiece(), None, RedPiece()],
    [RedPiece(), None, RedPiece(), None, RedPiece(), None, RedPiece(), None]
]
START_PIECE_COUNT = 12


class GameState:
    '''
        Class -- GameState
            Represents the game state.
    '''
    def __init__(self):
        '''
            Constructor -- creates a new instance of GameState
            Parameters:
                self -- the current GameState object.
        '''
        self.cur_plyr = BLK
        self.op_plyr = RED
        self.num_blk = START_PIECE_COUNT
        self.num_red = START_PIECE_COUNT
        self._board = DEFAULT_BOARD
        self.pos_moves = self.avail_moves(self.cur_plyr)
        self._selection_made = False
        self._sel_pce_row = None
        self._sel_pce_col = None
        self._sel_pce = None
        self._sel_pce_mvs = None

    def swap_turn(self):
        '''
            Method -- swap_turn
                Swaps which colors turn it is.
            Parameters:
                self -- the current GameState object.
            Returns:
                Nothing.
        '''
        self.cur_plyr, self.op_plyr = self.op_plyr, self.cur_plyr
        self.pos_moves = self.avail_moves(self.cur_plyr)

    def game_over(self):
        '''
            Method -- game_over
                Checks to see if either player has met the conditions of
                defeat.
            Parameters:
                self -- the current GameState object.
            Returns:
                False if both players still have pieces with at least one that
                can move. Otherwise returns true and defines the winner
                attribute according to the winning color.
        '''
        return self.num_blk == 0 or self.num_red == 0 or len(self.pos_moves) == 0

    def avail_moves(self, plyr: str) -> Set[Tuple[int, int]]:
        moves = set()

        for i, row in enumerate(self._board):
            for j, sq in enumerate(row):
                if sq and sq.get_color() == plyr:
                    for new_sq in sq.get_moves(i, j, self._board):
                        moves.add(new_sq)

        return moves

    def get_board(self) -> List[List[Piece]]:
        return self._board

    def get_cur_player(self) -> str:
        return self.cur_plyr

    def get_avail_moves(self) -> Set[Tuple[int, int]]:
        return self.pos_moves

    def get_selected_piece_moves(self) -> Set[Tuple[int, int]]:
        return self._sel_pce_mvs

    def selection_made(self) -> bool:
        return self._selection_made

    def select_piece(self, pce_row: int, pce_col: int, moves: Set[Tuple[int, int]]) -> None:
        self._selection_made = True
        self._sel_pce_row = pce_row
        self._sel_pce_col = pce_col
        self._sel_pce = self._board[pce_row][pce_col]
        self._sel_pce_mvs = moves

    def unselect_piece(self) -> None:
        self._selection_made = False
        self._sel_pce_row = None
        self._sel_pce_col = None
        self._sel_pce = None
        self._sel_pce_mvs = None

    def _capture_move(self, new_row: int, new_col: int) -> None:
        cap_row = min(new_row, self._sel_pce_row) + 1
        cap_col = min(new_col, self._sel_pce_col) + 1
        cap_piece = self._board[cap_row][cap_col]
        if cap_piece.get_color() == BLK:
            self.num_blk -= 1
        else:
            self.num_red -= 1
        self._board[cap_row][cap_col] = None

    def move_piece(self, new_row: int, new_col: int) -> None:
        if abs(new_row - self._sel_pce_row) == 2:
            self._capture_move(new_row, new_col)
        if (new_row == 0 or new_row == len(self._board) - 1) and \
           self._sel_pce.get_rank() != KNG:
           self._sel_pce.rank_up()
        self._board[new_row][new_col] = self._sel_pce
        self._board[self._sel_pce_row][self._sel_pce_col] = None
        self.unselect_piece()

    def get_winner(self) -> str:
        if self.num_blk == 0 or (self.op_plyr == BLK and len(self.pos_moves) == 0):
            return BLK
        if self.num_red == 0 or (self.op_plyr == RED and len(self.pos_moves) == 0):
            return RED
        return None
