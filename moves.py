'''
Jake Van Meter
CS5001 Fall 2021
Moves class. Handles the movement logic for regular and king checker pieces
based on their color.
'''
from constants import EMPTY, UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT,\
    CAP_UP_R, CAP_UP_L, CAP_DOWN_R, CAP_DOWN_L, MIN_BOUND, MAX_BOUND


class Moves:
    '''
        Class -- Moves
            Represents the moves available to pieces on the checkerboard.
        Attributes:
            player -- the color of the player whose piece will be moved.
            board -- the gameboard on which a move will occur.
            available_moves -- list containing the moves available to a given
                               piece.
        Methods:
            blk_reg -- handles movement logic for regular black pieces.
            red_reg -- handles movement logic for regular red pieces.
            king -- handles movement logic for king pieces.
            force_capture -- if a capture is possible for a given piece,
                             removes all other non-capture moves.
    '''
    def __init__(self, player, board):
        '''
            Constructor -- creates a new instance of Moves.
            Parameters:
                self -- the current Moves object.
                player -- the checker color to be moved (i.e. RED or BLACK).
                board -- the board on which the move will occur.
        '''
        self.player = player
        self.board = board
        self.available_moves = []

    def blk_reg(self, row, col):
        '''
            Method -- blk_reg
                Handles the movement logic available to a regular black piece.
                If a given move is possible, appends it to available_move
                attribute.
            Parameters:
                self -- the current Moves object.
                row -- the row index of the piece that is being moved.
                col -- the column index of the piece that is being moved.
            Returns:
                Nothing. Appends potential moves to available_moves attribute.
        '''
        player = self.player
        board = self.board
        up = row + 1
        right = col + 1
        left = col - 1
        # Check that up is within index
        if up <= MAX_BOUND:
            # Check that right is within index
            if right <= MAX_BOUND:
                # If spot is empty add to available moves
                if board[up][right] == EMPTY:
                    self.available_moves.append(UP_RIGHT)
                # If spot is opposite color piece check if capture possible
                elif board[up][right] % player != 0:
                    if up + 1 <= MAX_BOUND and right + 1 <= MAX_BOUND and\
                       board[up + 1][right + 1] == EMPTY:
                        self.available_moves.append(CAP_UP_R)
            # Check that left is within index
            if left >= MIN_BOUND:
                # If spot is empty add to avaiable moves
                if board[up][left] == EMPTY:
                    self.available_moves.append(UP_LEFT)
                # If spot is opposite color piece check if capture possible
                elif board[up][left] % player != 0:
                    if up + 1 <= MAX_BOUND and left - 1 >= MIN_BOUND and\
                       board[up + 1][left - 1] == EMPTY:
                        self.available_moves.append(CAP_UP_L)

    def red_reg(self, row, col):
        '''
            Method -- red_reg
                Handles the movement logic available to a regular red piece.
                If a given move is possible, appends it to available_move
                attribute.
            Parameters:
                self -- the current Moves object.
                row -- the row index of the piece that is being moved.
                col -- the column index of the piece that is being moved.
            Returns:
                Nothing. Appends potential moves to available_moves attribute.
        '''
        player = self.player
        board = self.board
        down = row - 1
        right = col + 1
        left = col - 1
        # Check that down is within index
        if down >= MIN_BOUND:
            # Check that right is within index
            if right <= MAX_BOUND:
                # If spot is empty add to available moves
                if board[down][right] == EMPTY:
                    self.available_moves.append(DOWN_RIGHT)
                # If spot is opposite color piece check if capture possible
                elif board[down][right] % player != 0:
                    if down - 1 >= MIN_BOUND and right + 1 <= MAX_BOUND and\
                       board[down - 1][right + 1] == EMPTY:
                        self.available_moves.append(CAP_DOWN_R)
            # Check that left is within index
            if left >= MIN_BOUND:
                # If spot is empty add to available moves
                if board[down][left] == EMPTY:
                    self.available_moves.append(DOWN_LEFT)
                # If spot is opposite color piece check if capture possible
                elif board[down][left] % player != 0:
                    if down - 1 >= MIN_BOUND and left - 1 >= MIN_BOUND and\
                       board[down - 1][left - 1] == EMPTY:
                        self.available_moves.append(CAP_DOWN_L)

    def king(self, row, col):
        '''
            Method -- king
                Handles the movement logic available to king pieces by
                treating it as a combination of a regular black and regular
                black piece.
            Parameters:
                self -- the current Moves object.
                row -- the row index of the piece that is being moved.
                col -- the column index of the piece that is being moved.
            Returns:
                Nothing. Appends potential moves to available_moves attribute.
        '''
        self.blk_reg(row, col)
        self.red_reg(row, col)

    def force_capture(self):
        '''
            Method -- force_capture
                Forces a piece to execute only capture moves if possible by
                removing non-capture moves from the available_moves attribute.
            Parameters:
                self -- the current Moves object.
            Returns:
                Nothing.
        '''
        # If capture possible force capture
        if CAP_UP_R in self.available_moves or\
           CAP_UP_L in self.available_moves or\
           CAP_DOWN_R in self.available_moves or\
           CAP_DOWN_L in self.available_moves:
            if UP_RIGHT in self.available_moves:
                self.available_moves.remove(UP_RIGHT)
            if UP_LEFT in self.available_moves:
                self.available_moves.remove(UP_LEFT)
            if DOWN_RIGHT in self.available_moves:
                self.available_moves.remove(DOWN_RIGHT)
            if DOWN_LEFT in self.available_moves:
                self.available_moves.remove(DOWN_LEFT)
