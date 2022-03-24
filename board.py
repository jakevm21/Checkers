'''
Jake Van Meter
CS5001 Fall 2021
Board class. Manages the logic for all interactions on the checkerboard. This
includes converting clicks into checker square index positions, selection of
checkers, and movement of ai and human player checkers including capture moves.
'''
import random
from moves import Moves
from constants import EMPTY, BLACK, RED, K_BLACK, K_RED, DEFAULT_BOARD,\
    NUM_SQUARES, SQUARE, UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT, CAP_UP_R,\
    CAP_UP_L, CAP_DOWN_R, CAP_DOWN_L, MIN_BOUND, MAX_BOUND


class Board:
    '''
        Class -- Board
            Represents the checkerboard.
        Attributes:
            board -- the current gameboard with updated piece positions.
            x -- location of mouse click along the x-axis.
            y -- location of mouse click along the y-axis.
            axis_size -- size of half the overall board size.
            square_size -- size of a single side of a checkerboard square.
            s_p_col -- index of the selected piece's column.
            s_p_row -- index of the selected piece's row.
            red_pieces -- remaining red pieces.
            black_pieces -- remaining black pieces.
            clicked_row -- index of the row clicked by mouse.
            clicked_col -- index of the column clicked by the mouse.
            available_moves -- list containing moves available to a piece.
        Methods:
            out_of_bounds -- checks if a mouse click was outside boundary of
                checkerboard.
            click_to_row -- converts a click's location on y-axis to an
                associated row index position.
            click_to_col -- converts a click's location on x-axis to an
                associated column index position.
            is_player_square -- determines whether a piece in a given square
                belongs to the player.
            is_movable_piece -- determeines whether a given piece is movable.
            valid_move -- determines whether an attempted move is valid.
            move_piece -- moves a piece to its new location on checkerboard.
            ai_move -- executes the turn for ai player.
            movable_pieces -- creates a list containing ordered pairs with the
                row and column indices of a piece that can move.
            move_count -- counts the number moves available to a certain color.
    '''
    def __init__(self):
        '''
            Constructor -- creates a new instance of Board.
            Parameters:
                self -- the current Board object.
        '''
        self.board = DEFAULT_BOARD
        self.x = 0
        self.y = 0
        self.axis_size = 200
        self.square_size = 50
        self.s_p_col = 0
        self.s_p_row = 0
        self.red_pieces = 12
        self.black_pieces = 12

    def out_of_bounds(self):
        '''
            Method -- out_of_bounds
                Checks if a click was outside the bounds of the checkerboard.
            Parameter:
                self -- the current Board object.
            Returns:
                True if the click was out of bounds. False otherwise.
        '''
        x = self.x
        y = self.y
        OUT_OF_BOUNDS = NUM_SQUARES * SQUARE / 2
        return x < -OUT_OF_BOUNDS or y < -OUT_OF_BOUNDS or\
            x > OUT_OF_BOUNDS or y > OUT_OF_BOUNDS

    def click_to_row(self):
        '''
            Method -- click_to_row
                Converts the location of the user's mouse click into an
                integer associated with that click's location on the board's
                y axis. This integer can then be used to access the associated
                index position of the square's row.
            Parameter:
                self -- the current Board object
            Returns:
                Nothing.
        '''
        try:
            # If the click is on the bottom half of the board
            # (i.e. y is negative)
            if self.y < 0:
                row = (self.axis_size - abs(self.y)) // self.square_size
            # If the click is on the upper half of the board
            # (i.e. y is positive)
            elif self.y >= 0:
                row = (self.axis_size + self.y) // self.square_size
            self.clicked_row = int(row)
        except IndexError:
            pass

    def click_to_col(self):
        '''
            Method -- click_to_col
                Converts the location of the user's mouse click into an
                integer associated with that click's location on the board's
                x axis. This integer can then be used to access the associated
                index position of the square's column.
            Parameter:
                self -- the current Board object.
            Returns:
                Nothing.
        '''
        try:
            # If the click is on the left half of the board
            # (i.e. x is negative)
            if self.x < 0:
                col = (self.axis_size - abs(self.x)) // self.square_size
            # If the click is on the right half of the board
            # (i.e. x is positive)
            elif self.x >= 0:
                col = (self.axis_size + self.x) // self.square_size
            self.clicked_col = int(col)
        except IndexError:
            pass

    def is_player_square(self, current_player):
        '''
            Method -- is_player_square
                Checks that the clicked on square contains a piece belonging
                to current player.
            Parameters:
                self -- the current Board object.
                current_player -- the player whose turn it is.
            Returns:
                True if the clicked location is associated with one of the
                current player's pieces. False otherwise.
        '''
        clicked_location = self.board[self.clicked_row][self.clicked_col]

        # Check that player clicked on a square containing one of their pieces
        if clicked_location == current_player or\
           clicked_location == (current_player + 2):
            print("That's your piece!")
            return True
        print("That's not your piece!")
        return False

    def is_movable_piece(self, current_player):
        '''
            Method -- is_movable_piece
                Checks that the clicked on piece is able to move.
            Parameters:
                self -- the current Board object.
                current_player -- the player whose turn it is.
            Returns:
                True if there are available moves for the selected piece. False
                otherwise.
        '''
        # Variables used in determining potential moves
        board = self.board
        moves = Moves(current_player, board)
        row = self.clicked_row
        col = self.clicked_col
        # Stores which moves are available to selected piece
        self.available_moves = []

        # Moves available to black
        if current_player == BLACK:
            # Regular piece
            if board[row][col] == BLACK:
                moves.blk_reg(row, col)
            # King piece
            elif board[row][col] == K_BLACK:
                moves.king(row, col)
        # Moves available to red regular pieces
        elif current_player == RED:
            # Regular piece
            if board[row][col] == RED:
                moves.red_reg(row, col)
            # King piece
            elif board[row][col] == K_RED:
                moves.king(row, col)

        # If capture possible, force capture
        moves.force_capture()

        self.available_moves = moves.available_moves
        moves.available_moves = []

        return len(self.available_moves) > 0

    def valid_move(self):
        '''
            Method -- valid_move
                Determines whether an attempted move by the player was valid.
            Parameter:
                self -- the current Board object.
            Returns:
                True if the attempted move was valid. False otherwise.
        '''
        row = self.clicked_row
        col = self.clicked_col
        s_p_row = self.s_p_row
        s_p_col = self.s_p_col
        available_moves = self.available_moves
        board = self.board

        if row == s_p_row + 1:
            if s_p_col + 1 == col and UP_RIGHT in available_moves:
                if board[row][col] == EMPTY:
                    return True
            elif s_p_col - 1 == col and UP_LEFT in available_moves:
                if board[row][col] == EMPTY:
                    return True
        elif row == s_p_row - 1:
            if s_p_col + 1 == col and DOWN_RIGHT in available_moves:
                if board[row][col] == EMPTY:
                    return True
            elif s_p_col - 1 == col and DOWN_LEFT in available_moves:
                if board[row][col] == EMPTY:
                    return True
        elif row == s_p_row + 2:
            if s_p_col + 2 == col and CAP_UP_R in available_moves:
                if board[row][col] == EMPTY:
                    return True
            elif s_p_col - 2 == col and CAP_UP_L in available_moves:
                if board[row][col] == EMPTY:
                    return True
        elif row == s_p_row - 2:
            if (s_p_col + 2 == col and CAP_DOWN_R in available_moves) or\
               (s_p_col - 2 == col and CAP_DOWN_L in available_moves):
                if board[row][col] == EMPTY:
                    return True

    def move_piece(self, current_player):
        '''
            Method -- move_piece
                Carries out a move by a certain color player by changing its
                location in the board attribute. If capture is made, erases the
                captured piece from the board.
            Parameters:
                self -- the current Board object.
                current_player -- the color of the piece being moved.
            Returns:
                Nothing.
        '''
        row = self.clicked_row
        col = self.clicked_col
        s_p_row = self.s_p_row
        s_p_col = self.s_p_col
        capture_made = False

        # If the move was a capture move, erase the captured piece
        if row == s_p_row + 2 or row == s_p_row + 4:
            if col == s_p_col + 2:
                self.board[row - 1][col - 1] = EMPTY
            elif col == s_p_col - 2:
                self.board[row - 1][col + 1] = EMPTY
            capture_made = True
        elif row == s_p_row - 2 or row == s_p_row - 4:
            if col == s_p_col + 2:
                self.board[row + 1][col - 1] = EMPTY
            elif col == s_p_col - 2:
                self.board[row + 1][col + 1] = EMPTY
            capture_made = True

        if capture_made:
            if current_player == BLACK:
                self.red_pieces -= 1
            elif current_player == RED:
                self.black_pieces -= 1

        # If the piece reaches opposite end of board convert to King
        if row == MAX_BOUND and self.board[s_p_row][s_p_col] == BLACK:
            self.board[row][col] = K_BLACK
        elif row == MIN_BOUND and self.board[s_p_row][s_p_col] == RED:
            self.board[row][col] = K_RED
        else:
            self.board[row][col] = self.board[s_p_row][s_p_col]

        self.board[s_p_row][s_p_col] = EMPTY
        self.available_moves = []

    def ai_move(self, ai_color):
        '''
            Method -- ai_move
                Carries out an ai player's turn. Starts by compiling all the
                potential pieces that can be moved by the ai then randomly
                selects one. After randomly selecting one, it randomly selects
                a move that is available to that piece. Finishes by moving
                the piece according to that randomly selected move.
            Parameters:
                self -- the current Board object.
                ai_color -- the color that the ai is playing as.
            Returns:
                Nothing.
        '''
        # Store index locations of ai pieces that are movable
        potential_pieces = self.movable_pieces(ai_color)
        # Choose a random piece to move
        piece = random.choice(potential_pieces)
        row = piece[0]
        col = piece[1]
        self.clicked_row = row
        self.clicked_col = col
        self.s_p_row = row
        self.s_p_col = col
        self.is_movable_piece(ai_color)
        chosen_move = random.choice(self.available_moves)
        if chosen_move == UP_LEFT:
            self.clicked_row += 1
            self.clicked_col -= 1
        elif chosen_move == UP_RIGHT:
            self.clicked_row += 1
            self.clicked_col += 1
        elif chosen_move == DOWN_LEFT:
            self.clicked_row -= 1
            self.clicked_col -= 1
        elif chosen_move == DOWN_RIGHT:
            self.clicked_row -= 1
            self.clicked_col += 1
        elif chosen_move == CAP_UP_L:
            self.clicked_row += 2
            self.clicked_col -= 2
        elif chosen_move == CAP_UP_R:
            self.clicked_row += 2
            self.clicked_col += 2
        elif chosen_move == CAP_DOWN_L:
            self.clicked_row -= 2
            self.clicked_col -= 2
        elif chosen_move == CAP_DOWN_R:
            self.clicked_row -= 2
            self.clicked_col += 2
        self.move_piece(ai_color)

    def movable_pieces(self, current_player):
        '''
            Method -- movable_pieces
                Collects all of the pieces that are able to be moved by a given
                player color.
            Parameters:
                self -- the current Board object.
                current_player -- the color whose pieces are being checked.
            Returns:
                A list containing the ordered pairs representing the indices
                of the pieces that can be moved. With the row index position in
                the first position and the column index position in the second
                position.
        '''
        # Variable to store the ordered pairs that represent a movable piece's
        # row and column index position as (row, col)
        movable_pieces = []
        piece_row = -1
        piece_col = -1
        for row in self.board:
            piece_row += 1
            for col in row:
                piece_col += 1
                self.clicked_row = piece_row
                self.clicked_col = piece_col
                if self.is_movable_piece(current_player):
                    movable_pieces.append((piece_row, piece_col))
            piece_col = -1
        return movable_pieces

    def move_count(self, player):
        '''
            Method -- move_count
                Counts the number of movable pieces that a given color has.
            Parameters:
                self -- the current Board object.
                player -- the color whose movable pieces are being counted.
            Returns:
                An integer representing the number of pieces that have
                potential moves available to them.
        '''
        available_moves = self.available_moves
        moveable_pieces = self.movable_pieces(player)
        self.available_moves = available_moves
        return len(moveable_pieces)
