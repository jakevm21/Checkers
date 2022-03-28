'''
Jake Van Meter
CS5001 Fall 2021
Final Project.
'''
import turtle
from gamestate import GameState
from board import Board
from constants import BLACK, RED, NUM_SQUARES, SQUARE, UP_RIGHT, UP_LEFT,\
    DOWN_RIGHT, DOWN_LEFT, CAP_UP_R, CAP_UP_L, CAP_DOWN_R, CAP_DOWN_L,\
    SQUARE_COLORS, CHECKER_COLORS, CHECKER_POSITION, CHECKER_SIZE,\
    BOARD_SIZE, WINDOW_SIZE, DEFAULT_POSITION, K_BLACK, K_RED


# Instance of GameState class
GAMESTATE = GameState()
# Instance of Board class
BOARD = Board()


def setup():
    # Create the UI window. Size is width of the board plus a little margin
    turtle.setup(WINDOW_SIZE, WINDOW_SIZE)

    # Set the drawing canvas size. The should be actual board size
    turtle.screensize(BOARD_SIZE, BOARD_SIZE)
    turtle.bgcolor("white")  # The window's background color
    turtle.tracer(0, 0)  # makes the drawing appear immediately


def click_handler(x, y):
    '''
        Function -- click_handler
            Called when a click occurs.
        Parameters:
            x -- X coordinate of the click. Automatically provided by Turtle.
            y -- Y coordinate of the click. Automatically provided by Turtle.
        Returns:
            Does not and should not return. Click handlers are a special type
            of function automatically called by Turtle. You will not have
            access to anything returned by this function.
    '''
    # Draw the board and squares after each click
    pen = turtle.Turtle()
    pen.penup()  # This allows the pen to be moved
    pen.hideturtle()  # This gets rid of the triangle cursor
    draw_board_squares(pen)

    print("Clicked at", x, y)

    BOARD.x = x
    BOARD.y = y

    # Updated board
    board = BOARD.board
    # Current player
    player = GAMESTATE.current_player
    # AI player color
    ai_player = GAMESTATE.ai_player_color

    # Inform user if click was out of bounds
    if BOARD.out_of_bounds():
        print("Click was out of bounds!")
        return None

    # If click was inbounds assign the x and y coordinates to game state
    else:
        # Turn the x and y coordinates into index positions associated with
        # the clicked square on the board
        BOARD.click_to_col()
        BOARD.click_to_row()
        # Store the col and row index positions
        col = BOARD.clicked_col
        row = BOARD.clicked_row

        # Check if a piece was already selected on a prior click
        if GAMESTATE.piece_selected:
            # Check if click is a valid move
            if BOARD.valid_move():
                BOARD.move_piece(player)
                GAMESTATE.piece_selected = False
                draw_board_squares(pen)
                # If the game is being played against the computer
                if GAMESTATE.ai_player:
                    # # If the ai player can move
                    # if BOARD.move_count(ai_player) > 0:
                    BOARD.ai_move(ai_player)
                    draw_board_squares(pen)
                # Otherwise swap to other player's turn
                else:
                    GAMESTATE.swap_turn()
            # If click is not a valid move keep the selected piece and its
            # available moves highlighted
            else:
                select_checker(pen, BOARD.s_p_col, BOARD.s_p_row)
                draw_available_moves(pen, BOARD.s_p_col, BOARD.s_p_row)
                draw_checkers(pen, BOARD.s_p_col, BOARD.s_p_row, board)

        # Check that the clicked square contains current player's piece
        elif BOARD.is_player_square(player):
            # Check that the clicked piece is movable and if movable highlight
            # available moves
            if BOARD.is_movable_piece(player):
                print("It's movable!")
                GAMESTATE.piece_selected = True
                # Store the selected piece's index positions
                BOARD.s_p_col = col
                BOARD.s_p_row = row
                select_checker(pen, col, row)
                draw_available_moves(pen, col, row)
                draw_checkers(pen, col, row, board)

        # Check if game over conditions have been met
        if GAMESTATE.game_over(BOARD.red_pieces, BOARD.black_pieces,
                               BOARD.move_count(RED), BOARD.move_count(BLACK)):
            victory_message(GAMESTATE.winner)


def draw_square(a_turtle, size):
    '''
        Function -- draw_square
            Draw a square of a given size.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the square
        Returns:
            Nothing. Draws a square in the graphics window.
    '''
    RIGHT_ANGLE = 90
    a_turtle.pendown()
    a_turtle.begin_fill()
    for i in range(4):
        a_turtle.forward(size)
        a_turtle.left(RIGHT_ANGLE)
    a_turtle.end_fill()
    a_turtle.penup()


def draw_circle(a_turtle, size):
    '''
        Function -- draw_circle
            Draw a circle with a given radius.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the radius of the circle
        Returns:
            Nothing. Draws a circle in the graphics window.
    '''
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.circle(size)
    a_turtle.end_fill()
    a_turtle.penup()


def draw_board(a_turtle):
    '''
        Function -- draw_board
            Draws the outline of the board of a predefined size.
        Parameters:
            a_turtle -- an instance of Turtle
        Returns:
            Nothing. Draws the board in the graphics window.
    '''
    # Board outline is black, filler is white
    a_turtle.color("black", "white")
    # Outline of checkerboard
    a_turtle.setposition(DEFAULT_POSITION, DEFAULT_POSITION)
    draw_square(a_turtle, BOARD_SIZE)


def draw_board_squares(a_turtle):
    '''
        Function -- draw_board_squares
            Draws the checker board squares.
        Parameters:
            a_turtle -- an instance of Turtle.
        Returns:
            Nothing. Draws the squares in the graphics window.
    '''
    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            # Places pen in bottom left of each square
            a_turtle.setposition(DEFAULT_POSITION + SQUARE * col,
                                 DEFAULT_POSITION + SQUARE * row)
            # Draw a square at every other square
            if col % 2 != row % 2:
                # Outline is black, filling is light gray
                a_turtle.color("black", SQUARE_COLORS[0])
                draw_square(a_turtle, SQUARE)
                # Draw the checkers
                draw_checkers(a_turtle, col, row, BOARD.board)


def draw_checkers(a_turtle, col, row, board):
    '''
        Function -- draw_checkers
            Draws a checker based on its index positions in a given
            checker board.
        Parameters:
            a_turtle -- an instance of Turtle.
            col -- the column index position of the checker.
            row -- the row index position of the checker.
            board -- the current game board.
        Returns:
            Nothing. Draws a checker in the graphics window.
    '''
    CROWN_POS = 7
    CROWN_SIZE = CHECKER_SIZE * 0.7
    # Set the turtle in position to draw a checker
    x_pos = DEFAULT_POSITION + (SQUARE * col) + CHECKER_POSITION
    y_pos = DEFAULT_POSITION + SQUARE * row
    a_turtle.setposition(x_pos, y_pos)
    # Draw black checkers
    if board[row][col] == BLACK:
        a_turtle.color(CHECKER_COLORS[0])
        draw_circle(a_turtle, CHECKER_SIZE)
    elif board[row][col] == K_BLACK:
        a_turtle.color(CHECKER_COLORS[0])
        draw_circle(a_turtle, CHECKER_SIZE)
        a_turtle.setposition(x_pos, y_pos + CROWN_POS)
        a_turtle.color("white", CHECKER_COLORS[0])
        draw_circle(a_turtle, CROWN_SIZE)
    # Draw red checkers
    elif board[row][col] == RED:
        a_turtle.color(CHECKER_COLORS[1])
        draw_circle(a_turtle, CHECKER_SIZE)
    elif board[row][col] == K_RED:
        a_turtle.color(CHECKER_COLORS[1])
        draw_circle(a_turtle, CHECKER_SIZE)
        a_turtle.setposition(x_pos, y_pos + CROWN_POS)
        a_turtle.color("white", CHECKER_COLORS[1])
        draw_circle(a_turtle, CROWN_SIZE)


def select_checker(a_turtle, col, row):
    '''
        Function -- select_checker
            Draws a blue outline around the selected checker.
        Parameters:
            a_turtle -- an instance of Turtle.
            col -- the column index of the selected checker.
            row -- the row index of the selected checker.
        Returns:
            Nothing.
    '''
    # Draw an outline around the square of the selected checker
    a_turtle.setposition(DEFAULT_POSITION + SQUARE * col,
                         DEFAULT_POSITION + SQUARE * row)
    # Make the outline blue
    a_turtle.color(SQUARE_COLORS[2], SQUARE_COLORS[0])
    draw_square(a_turtle, SQUARE)


def draw_available_moves(a_turtle, col, row):
    '''
        Function -- draw_available_moves
            Draws a red outline around the squares that a selected checker
            can move to.
        Parameters:
            a_turtle -- an instance of Turtle.
            col -- the column index of the checker to be moved.
            row -- the row index of the checker to be moved.
        Returns:
            Nothing.
    '''
    # Make the outline red
    a_turtle.color(SQUARE_COLORS[3], SQUARE_COLORS[0])
    # Stores the drawn available moves
    drawn_available_moves = []

    while len(BOARD.available_moves) > 0:
        # Draw outline around the upper right
        if UP_RIGHT in BOARD.available_moves:
            a_turtle.setposition(DEFAULT_POSITION + SQUARE * (col + 1),
                                 DEFAULT_POSITION + SQUARE * (row + 1))
            draw_square(a_turtle, SQUARE)
            drawn_available_moves.append(UP_RIGHT)
            BOARD.available_moves.remove(UP_RIGHT)
        # Draw outline around the upper left
        elif UP_LEFT in BOARD.available_moves:
            a_turtle.setposition(DEFAULT_POSITION + SQUARE * (col - 1),
                                 DEFAULT_POSITION + SQUARE * (row + 1))
            draw_square(a_turtle, SQUARE)
            drawn_available_moves.append(UP_LEFT)
            BOARD.available_moves.remove(UP_LEFT)
        # Draw outline around the lower right
        elif DOWN_RIGHT in BOARD.available_moves:
            a_turtle.setposition(DEFAULT_POSITION + SQUARE * (col + 1),
                                 DEFAULT_POSITION + SQUARE * (row - 1))
            draw_square(a_turtle, SQUARE)
            drawn_available_moves.append(DOWN_RIGHT)
            BOARD.available_moves.remove(DOWN_RIGHT)
        # Draw outline around the lower left
        elif DOWN_LEFT in BOARD.available_moves:
            a_turtle.setposition(DEFAULT_POSITION + SQUARE * (col - 1),
                                 DEFAULT_POSITION + SQUARE * (row - 1))
            draw_square(a_turtle, SQUARE)
            drawn_available_moves.append(DOWN_LEFT)
            BOARD.available_moves.remove(DOWN_LEFT)
        # Draw outline around capture move to upper right
        elif CAP_UP_R in BOARD.available_moves:
            a_turtle.setposition(DEFAULT_POSITION + SQUARE * (col + 2),
                                 DEFAULT_POSITION + SQUARE * (row + 2))
            draw_square(a_turtle, SQUARE)
            drawn_available_moves.append(CAP_UP_R)
            BOARD.available_moves.remove(CAP_UP_R)
        # Draw outline around capture move to upper left
        elif CAP_UP_L in BOARD.available_moves:
            a_turtle.setposition(DEFAULT_POSITION + SQUARE * (col - 2),
                                 DEFAULT_POSITION + SQUARE * (row + 2))
            draw_square(a_turtle, SQUARE)
            drawn_available_moves.append(CAP_UP_L)
            BOARD.available_moves.remove(CAP_UP_L)
        # Draw outline around capture move to lower right
        elif CAP_DOWN_R in BOARD.available_moves:
            a_turtle.setposition(DEFAULT_POSITION + SQUARE * (col + 2),
                                 DEFAULT_POSITION + SQUARE * (row - 2))
            draw_square(a_turtle, SQUARE)
            drawn_available_moves.append(CAP_DOWN_R)
            BOARD.available_moves.remove(CAP_DOWN_R)
        # Draw outline around capture move to lower left
        elif CAP_DOWN_L in BOARD.available_moves:
            a_turtle.setposition(DEFAULT_POSITION + SQUARE * (col - 2),
                                 DEFAULT_POSITION + SQUARE * (row - 2))
            draw_square(a_turtle, SQUARE)
            drawn_available_moves.append(CAP_DOWN_L)
            BOARD.available_moves.remove(CAP_DOWN_L)

    # Re-add the available moves after drawing them for later use
    BOARD.available_moves = drawn_available_moves


def victory_message(winner):
    '''
        Function -- victory_message
            Draws a green message declaring the winner of the match.
        Parameters:
            winner -- the winner of the match.
        Returns:
            Nothing.
    '''
    pen = turtle.Turtle()
    font = "century"
    font_size = 30
    font_type = "bold"

    pen.setposition(DEFAULT_POSITION + BOARD_SIZE / 2,
                    DEFAULT_POSITION + 250)
    pen.color("green")
    pen.write("Game Over!", False, "center", (font, font_size, font_type))
    pen.setposition(DEFAULT_POSITION + BOARD_SIZE / 2,
                    DEFAULT_POSITION + 150)
    pen.write(f"{winner} Wins", False, "center", (font, font_size, font_type))


def main():
    num_players_selected = False
    while not num_players_selected:
        ai = input("How many players?\n1 -- One player\
                    \n2 -- Two players\n")
        if ai == "1":
            GAMESTATE.ai_player = True
            num_players_selected = True
            # player_color_selected = False
            # while not player_color_selected:
            #     color = input("What color would you like to play as?\
            #                   \n1 -- Black\n2 -- Red\n")
            #     if color == "1":
            #         player_color_selected = True
            #         self.ai_player_color = RED
            #     elif color == "2":
            #         player_color_selected = True
            #         self.ai_player_color = BLACK
            #     else:
            #         print("Invalid selection...")
        elif ai == "2":
            num_players_selected = True
        else:
            print("Invalid selection...")

    setup()
    pen = turtle.Turtle()  # Variable that will do the drawing
    pen.penup()  # This allows the pen to be moved
    pen.hideturtle()  # This gets rid of the triangle cursor
    draw_board(pen)
    draw_board_squares(pen)

    # Click handling
    screen = turtle.Screen()
    try:
        screen.onclick(click_handler)
    except IndexError:
        print("Click was out of bounds!")

    turtle.done()  # Stops the window from closing


if __name__ == "__main__":
    main()
