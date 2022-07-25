'''
Jake Van Meter
CS5001 Fall 2021
Gamestate class. Handles the logic regarding whose turn it is, whether there
is an ai player or two human players, and whether the game over conditions
have been met.
'''
from typing import Tuple
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
        self.num_blk = START_PIECE_COUNT
        self.num_red = START_PIECE_COUNT
        self.board = DEFAULT_BOARD
        self.winner = None

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
        else:
            self.cur_player = BLK

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
        return self.num_blk == 0 or self.num_red == 0

    def count_avail_moves(self) -> set[Tuple[int, int]]:
        for i, row in enumerate(self.board):
            for j, sq in enumerate(row):
                if sq and sq.get_color == self.cur_player:
                    # TODO: functionality to get moves
                    pass

    def get_winner(self) -> str:
        return self.winner

    def get_board(self):
        return self.board

    def get_cur_player(self):
        return self.cur_player
