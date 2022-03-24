'''
Jake Van Meter
CS5001 Fall 2021
Constants used by various project files.
'''
# Players
EMPTY = 0
BLACK = 2
RED = 3
K_BLACK = 4
K_RED = 9

# Piece ranks
REG = "regular"
KING = "king"

# Default board layout
DEFAULT_BOARD = [
        [EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK],
        [BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY],
        [EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [RED, EMPTY, RED, EMPTY, RED, EMPTY, RED, EMPTY],
        [EMPTY, RED, EMPTY, RED, EMPTY, RED, EMPTY, RED],
        [RED, EMPTY, RED, EMPTY, RED, EMPTY, RED, EMPTY]
]

# The number of squares on each row
NUM_SQUARES = 8
# The size of each square in the checkerboard
SQUARE = 50

# The possible colors for each square
SQUARE_COLORS = ("light gray", "white", "blue", "red")
# The possible colors for each checker
CHECKER_COLORS = ("black", "maroon")
# The postition of a checker within a single square
CHECKER_POSITION = SQUARE / 2
# The size of a checker's radius
CHECKER_SIZE = SQUARE / 2
# Size of the board
BOARD_SIZE = NUM_SQUARES * SQUARE
# Create the UI window. This should be the width of the board plus a
# little margin
WINDOW_SIZE = BOARD_SIZE + SQUARE  # The extra + SQUARE is the margin
# Default position of pen is bottom left
DEFAULT_POSITION = -BOARD_SIZE / 2 - 1

# Boundaries of board
MAX_BOUND = 7
MIN_BOUND = 0

# Normal move directions
UP_RIGHT = "up-right"
UP_LEFT = "up-left"
DOWN_RIGHT = "down-right"
DOWN_LEFT = "down-left"
# Capture move directions
CAP_UP_R = "cap-up-right"
CAP_UP_L = "cap-up-left"
CAP_DOWN_R = "cap-down-right"
CAP_DOWN_L = "cap-down-left"
