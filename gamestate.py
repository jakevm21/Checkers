'''
Jake Van Meter
CS5001 Fall 2021
Gamestate class. Handles the logic regarding whose turn it is, whether there
is an ai player or two human players, and whether the game over conditions
have been met.
'''
from constants import BLACK, RED


class GameState:
    '''
        Class -- GameState
            Represents the game state.
        Attributes:
            current_player -- the color whose turn it is.
            opposite_player -- the color whose turn is next.
            piece_selected -- boolean representing whether a piece has been
                selected to be move.
            ai_player -- boolean representing whether the ai is the opponent.
            ai_player_color -- the color the ai is playing as.
            winner -- the player who won the match.
        Methods:
            swap_turn -- swaps the color whose turn it is to move.
            game_over -- checks whether the one of the colors has lost.
    '''
    def __init__(self):
        '''
            Constructor -- creates a new instance of GameState
            Parameters:
                self -- the current GameState object.
        '''
        self.current_player = BLACK
        self.opposite_player = RED
        self.piece_selected = False
        self.ai_player = False
        self.ai_player_color = RED

    def swap_turn(self):
        '''
            Method -- swap_turn
                Swaps which colors turn it is.
            Parameters:
                self -- the current GameState object.
            Returns:
                Nothing.
        '''
        if self.current_player == BLACK:
            self.current_player = RED
            self.opposite_player = BLACK
        elif self.current_player == RED:
            self.current_player = BLACK
            self.opposite_player = RED

    def game_over(self, rem_red, rem_blk, red_move_cnt, blk_move_cnt):
        '''
            Method -- game_over
                Checks to see if either player has met the conditions of
                defeat. If so, then the causes the game to end.
            Parameters:
                self -- the current GameState object.
                rem_red -- the remaining number of red checker pieces.
                rem_blk -- the remaining number of black checker pieces.
                red_move_cnt -- the remaining number of red checkers that can
                    be moved.
                blk_move_cnt -- the remaining number of black checkers that can
                    be moved.
            Returns:
                False if both players still have pieces with at least one that
                can move. Otherwise returns true and defines the winner
                attribute according to the winning color.
        '''
        if rem_red > 0 and red_move_cnt > 0 and\
           rem_blk > 0 and blk_move_cnt > 0:
            return False

        else:
            if rem_red == 0 or red_move_cnt == 0:
                self.winner = "Black"
            elif rem_blk == 0 or blk_move_cnt == 0:
                self.winner = "Red"

        return True
