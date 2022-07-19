import turtle as turt
NUM_SQS = 8     # The number of squares on each row
SQ_SIZE = 50    # The size of each square in the checkerboard
SQ_COLOR = "light gray"
OUTLINE_COLOR = "black"

class GUI:
    def __init__(self, num_sqs=NUM_SQS, sq_size=SQ_SIZE) -> None:
        self.num_sqs = num_sqs
        self.sq_size = sq_size
        self.brd_size = num_sqs * sq_size         # Size of the board
        self.wndw_size = self.brd_size + sq_size  # The extra + SQUARE is the margin
        self.def_pos = -self.brd_size / 2 - 1     # Bottom left corner of board

        self._screen_setup()
        self.pen = self._initialize_turt()        # Variable that will do the drawing
        self.draw_board()
        

    def _screen_setup(self) -> None:
        BG_COLOR = "white"
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
    
    def draw_board(self) -> None:
        '''
            Function -- draw_board
                Draws the outline of the board of a predefined size.
            Parameters:
                a_turtle -- an instance of Turtle
            Returns:
                Nothing. Draws the board in the graphics window.
        '''
        # Board outline is black, filler is white
        self.pen.color("black", "white")
        # Outline of checkerboard
        self.pen.setposition(self.def_pos, self.def_pos)
        self._draw_square(self.brd_size)
    
    def _draw_all_squares(self) -> None:
        for col in range(self.num_sqs):
            for row in range(self.num_sqs):
                # Places pen in bottom left of each square
                self.pen.setposition(self.def_pos + self.sq_size * col,
                                     self.def_pos + self.sq_size * row)
                # Draw a square at every other square
                if col % 2 != row % 2:
                    self._draw_square(self.sq_size)

    def _draw_square(self, size) -> None:
            RIGHT_ANGLE = 90
            self.pen.color(OUTLINE_COLOR, SQ_COLOR)  # Outline is black, filling is light gray
            self.pen.pendown()
            self.pen.begin_fill()
            for _ in range(4):
                self.pen.forward(size)
                self.pen.left(RIGHT_ANGLE)
            self.pen.end_fill()
            self.pen.penup()

    def draw_checker(self, col: int, row: int, color: str, rank: int) -> None:
        pass