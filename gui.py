import turtle as turt
from typing import Set, Tuple
from constants import *
from pieces import *


SQ_CLR = "light gray"
OUTLINE_CLR = "black"
BRD_BG_CLR = "white"
SEL_PCE_CLR = "blue"
MV_CLR = "red"
V_MSG_CLR = "green"
CROWN_CLR = "white"
CROWN_POS = 7

class GUI:
    def __init__(self, num_sqs=NUM_SQS, sq_size=SQ_SIZE) -> None:
        self._num_sqs = num_sqs
        self._sq_size = sq_size
        self._brd_size = num_sqs * sq_size         # Size of the board
        self._brd_x_max = self._brd_size / 2
        self._brd_x_min = -self._brd_x_max
        self._brd_y_max = self._brd_size / 2
        self._brd_y_min = -self._brd_y_max
        self._wndw_size = self._brd_size + sq_size  # The extra + SQUARE is the margin
        self._def_pos = (-self._brd_size / 2) - 1   # Bottom left corner of board
        self._piece_pos = self._sq_size / 2         # Center of a square
        self._piece_size = self._sq_size / 2
        self._crown_pos = CROWN_POS                # Position of crown on piece
        self._crown_size = self._piece_size * 0.7    # Size of crown on piece

        self._screen_setup()
        self.pen = self._initialize_turt()        # Variable that will do the drawing

    def _screen_setup(self) -> None:
        # Create the UI window. Size is width of the board plus a little margin
        turt.setup(self._wndw_size, self._wndw_size)

        # Set the drawing canvas size. The should be actual board size
        turt.screensize(self._brd_size, self._brd_size)
        turt.bgcolor(BRD_BG_CLR)  # The window's background color
        turt.tracer(0, 0)       # makes the drawing appear immediately
    
    def _initialize_turt(self) -> turt.Turtle:
        pen = turt.Turtle()
        pen.penup()             # This allows the pen to be moved
        pen.hideturtle()        # This gets rid of the triangle cursor
        return pen
    
    def draw_board(self, brd: List[List[Piece]]) -> None:
        '''
        Draws the checkerboard of a predefined size.

        Arguments:\n
        brd
            The board to be drawn.

        Returns:
            Nothing.
        '''
        # Board outline is black, filler is white
        self.pen.color(OUTLINE_CLR, BRD_BG_CLR)
        # Outline of checkerboard
        self.pen.setposition(self._def_pos, self._def_pos)
        self._draw_square(self._brd_size, OUTLINE_CLR, BRD_BG_CLR)
        # Each checkerboard square
        self._draw_all_squares(brd)

    def clear_board(self) -> None:
        '''
        Clears the board to be redrawn.
        '''
        self.pen.clear()

    def _draw_all_squares(self, brd: List[List[Piece]]) -> None:
        for i, row in enumerate(brd):
            for j, sq in enumerate(row):
                # Places pen in bottom left of each square
                x_pos = self._def_pos + (self._sq_size * j)
                y_pos = self._def_pos + (self._sq_size * i)
                self.pen.setposition(x_pos, y_pos)
                # Draw a square at every other square
                if i % 2 != j % 2:
                    self._draw_square(self._sq_size, OUTLINE_CLR, SQ_CLR)
                # Draw the checkers
                if sq:
                    self._draw_checker(x_pos + self._piece_pos, y_pos, sq)

    def _draw_square(self, size: int, outline_clr: str, fill_color: str) -> None:
            ANGLE = 90
            self.pen.color(outline_clr, fill_color)
            self.pen.pendown()
            self.pen.begin_fill()
            for _ in range(4):
                self.pen.forward(size)
                self.pen.left(ANGLE)
            self.pen.end_fill()
            self.pen.penup()

    def _draw_circle(self, size: int) -> None:
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(size)
        self.pen.end_fill()
        self.pen.penup()

    def _draw_checker(self, x_pos: float, y_pos: float, piece: Piece) -> None:
        self.pen.setposition(x_pos, y_pos)
        self.pen.color(piece.get_color())

        self._draw_circle(self._piece_size)
        # if piece is king draw crown
        if piece.get_rank() == KNG:
            self.pen.setposition(x_pos, y_pos + self._crown_pos)
            self.pen.pencolor(CROWN_CLR)
            self._draw_circle(self._crown_size)

    def victory_msg(self, winner: str) -> None:
        font = "century"
        font_size = 30
        font_type = "bold"
        x_pos = self._def_pos + self._brd_size / 2

        self.pen.setposition(x_pos, self._def_pos + 250)
        self.pen.color("green")
        self.pen.write(arg="Game Over!", 
                       move=False,
                       align="center",
                       font=(font, font_size, font_type))
        self.pen.setposition(x_pos, self._def_pos + 150)
        self.pen.write(arg=f"{winner.capitalize()} Wins",
                       move=False,
                       align="center",
                       font=(font, font_size, font_type))

    def click_to_square(self, x: float, y: float) -> Tuple[int, int]:
        if y < 0:
            row = self._brd_y_max - abs(y)
        else:
            row = self._brd_y_max + y
        row = int(row) // self._sq_size

        if x < 0:
            col = self._brd_x_max - abs(x)
        else:
            col = self._brd_x_max + x
        col = int(col) // self._sq_size

        return (row, col)

    def select_piece(self, row: int, col: int, piece: Piece, moves: Set[Tuple[int, int]]) -> None:
        x_pos = self._def_pos + (self._sq_size * col)
        y_pos = self._def_pos + (self._sq_size * row)

        # change outline to blue
        self.pen.setposition(x_pos, y_pos)
        self._draw_square(self._sq_size, SEL_PCE_CLR, SQ_CLR)
        # redraw piece
        self._draw_checker(x_pos + self._piece_pos, y_pos, piece)

        # draw moves
        for mv_row, mv_col in moves:
            x_pos = self._def_pos + (self._sq_size * mv_col)
            y_pos = self._def_pos + (self._sq_size * mv_row)
            self.pen.setposition(x_pos, y_pos)
            self._draw_square(self._sq_size, MV_CLR, SQ_CLR)

    def get_brd_size(self) -> int:
        return self._brd_size

    def get_x_max(self) -> int:
        return self._brd_x_max

    def get_x_min(self) -> int:
        return self._brd_x_min

    def get_y_max(self) -> int:
        return self._brd_y_max

    def get_y_min(self) -> int:
        return self._brd_y_min
