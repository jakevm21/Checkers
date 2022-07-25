import turtle as turt
from typing import List, Tuple
from piece_options import *
from pieces import Piece


SQ_COLOR = "light gray"
OUTLINE_COLOR = "black"
BG_COLOR = "white"
CROWN_POS = 7
SELECTION_COLOR = "blue"

class GUI:
    def __init__(self, num_sqs=NUM_SQS, sq_size=SQ_SIZE) -> None:
        self.num_sqs = num_sqs
        self.sq_size = sq_size
        self.brd_size = num_sqs * sq_size         # Size of the board
        self.brd_x_max = self.brd_size >> 1
        self.brd_x_min = -self.brd_x_max
        self.brd_y_max = self.brd_size >> 1
        self.brd_y_min = -self.brd_y_max
        self.wndw_size = self.brd_size + sq_size  # The extra + SQUARE is the margin
        self.def_pos = (-self.brd_size >> 1) - 1  # Bottom left corner of board
        self.piece_pos = self.sq_size >> 1        # Center of a square
        self.piece_size = self.sq_size >> 1
        self.crown_pos = CROWN_POS                # Position of crown on piece
        self.crow_size = self.piece_size * 0.7    # Size of crown on piece

        self._screen_setup()
        self.pen = self._initialize_turt()        # Variable that will do the drawing

    def _screen_setup(self) -> None:
        # Create the UI window. Size is width of the board plus a little margin
        turt.setup(self.wndw_size, self.wndw_size)

        # Set the drawing canvas size. The should be actual board size
        turt.screensize(self.brd_size, self.brd_size)
        turt.bgcolor(BG_COLOR)  # The window's background color
        turt.tracer(0, 0)       # makes the drawing appear immediately
    
    def _initialize_turt(self) -> turt.Turtle:
        pen = turt.Turtle()
        pen.penup()             # This allows the pen to be moved
        pen.hideturtle()        # This gets rid of the triangle cursor
        return pen
    
    def draw_board(self, brd: List[List[Piece]]) -> None:
        '''
            Function -- draw_board
                Draws the outline of the board of a predefined size.
            Parameters:
                a_turtle -- an instance of Turtle
            Returns:
                Nothing. Draws the board in the graphics window.
        '''
        # Board outline is black, filler is white
        self.pen.color(OUTLINE_COLOR, BG_COLOR)
        # Outline of checkerboard
        self.pen.setposition(self.def_pos, self.def_pos)
        self._draw_square(self.brd_size, OUTLINE_COLOR, BG_COLOR)
        # Each checkerboard square
        self._draw_all_squares(brd)
    
    def _draw_all_squares(self, brd: List[List[Piece]]) -> None:
        for i, row in enumerate(brd):
            for j, sq in enumerate(row):
                # Places pen in bottom left of each square
                x_pos = self.def_pos + (self.sq_size * j)
                y_pos = self.def_pos + (self.sq_size * i)
                self.pen.setposition(x_pos, y_pos)
                # Draw a square at every other square
                if i % 2 != j % 2:
                    self._draw_square(self.sq_size, OUTLINE_COLOR, SQ_COLOR)
                # Draw the checkers
                if sq:
                    self._draw_checker(sq.get_color(), sq.get_rank())

    def _draw_square(self, size: int, outline_color: str, fill_color: str) -> None:
            RIGHT_ANGLE = 90
            self.pen.color(outline_color, fill_color)
            self.pen.pendown()
            self.pen.begin_fill()
            for _ in range(4):
                self.pen.forward(size)
                self.pen.left(RIGHT_ANGLE)
            self.pen.end_fill()
            self.pen.penup()

    def _draw_circle(self, size):
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(size)
        self.pen.end_fill()
        self.pen.penup()

    def _draw_checker(self, color: str, rank: int) -> None:
        self.pen.color(color)

        self._draw_circle(self.piece_size)
        # if piece is king draw crown
        if rank == KNG:
            # TODO: Draw crown
            pass

    def click_to_square(self, x: float, y: float) -> Tuple[int, int]:
        if y < 0:
            row = self.brd_y_max - abs(y)
        else:
            row = self.brd_y_max + y
        row = int(row) // self.sq_size

        if x < 0:
            col = self.brd_x_max - abs(x)
        else:
            col = self.brd_x_max + x
        col = int(col) // self.sq_size

        return (row, col)

    def select_piece(self, row: int, col: int, piece: Piece) -> None:
        x_pos = self.def_pos + (self.sq_size * col)
        y_pos = self.def_pos + (self.sq_size * row)

        # change outline to blue
        self.pen.setposition(x_pos, y_pos)
        self._draw_square(self.sq_size, SELECTION_COLOR, SQ_COLOR)

        # redraw piece
        self.pen.setposition(x_pos + self.piece_pos, y_pos)
        self._draw_checker(piece.get_color(), piece.get_rank())

    def get_brd_size(self):
        return self.brd_size

    def get_x_max(self):
        return self.brd_x_max

    def get_x_min(self):
        return self.brd_x_min

    def get_y_max(self):
        return self.brd_y_max

    def get_y_min(self):
        return self.brd_y_min
