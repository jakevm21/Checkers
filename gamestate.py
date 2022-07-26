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
        self.cur_player = BLK
        self.op_player = RED
        self.num_blk = START_PIECE_COUNT
        self.num_red = START_PIECE_COUNT
        self.board = DEFAULT_BOARD
        self.pos_moves = self.avail_moves()

    def swap_turn(self):
        '''
            Method -- swap_turn
                Swaps which colors turn it is.
            Parameters:
                self -- the current GameState object.
            Returns:
                Nothing.
        '''
        if self.cur_player == BLK:
            self.cur_player = RED
            self.op_player = BLK
        else:
            self.cur_player = BLK
            self.op_player = RED
        self.pos_moves = self.avail_moves()

    def game_over(self):
        '''
            Method -- game_over
                Checks to see if either player has met the conditions of
                defeat. If so, then the causes the game to end.
            Parameters:
                self -- the current GameState object.
            Returns:
                False if both players still have pieces with at least one that
                can move. Otherwise returns true and defines the winner
                attribute according to the winning color.
        '''
        return self.num_blk == 0 or self.num_red == 0 or len(self.pos_moves) == 0

    def avail_moves(self) -> Set[Tuple[int, int]]:
        moves = set()

        for i, row in enumerate(self.board):
            for j, sq in enumerate(row):
                if sq and sq.get_color() == self.cur_player:
                    # TODO: functionality to get moves
                    for new_row, new_col in sq.get_moves(i, j):
                        new_sq = self.board[new_row][new_col]
                        if not new_sq:
                            moves.add((new_row, new_col))
                        elif new_sq.get_color() != self.cur_player:
                            # TODO: functionality to get capturing moves
                            for new_new_row, new_new_col in sq.get_moves(new_row, new_col):
                                new_new_sq = self.board[new_new_row][new_new_col]
                                if not new_new_sq:
                                    moves.add((new_new_row, new_new_col))

        return moves

    def get_board(self) -> List[List[Piece]]:
        return self.board

    def get_cur_player(self) -> str:
        return self.cur_player

    def get_avail_moves(self) -> Set[Tuple[int, int]]:
        return self.pos_moves
