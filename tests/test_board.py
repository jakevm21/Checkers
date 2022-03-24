'''
Jake Van Meter
CS5001 Fall 2021
Test file for Board class.
'''
import pytest
from board import Board
from constants import DEFAULT_BOARD, RED, BLACK


def test_constructor():
    board = Board()
    assert(board.board == DEFAULT_BOARD)
    assert(board.x == 0)
    assert(board.y == 0)
    assert(board.axis_size == 200)
    assert(board.square_size == 50)
    assert(board.s_p_col == 0)
    assert(board.s_p_row == 0)
    assert(board.red_pieces == 12)
    assert(board.black_pieces == 12)
    with pytest.raises(AttributeError):
        assert(board.clicked_row is None)
        assert(board.clicked_col is None)
        assert(board.available_moves is None)


def test_out_of_bounds():
    board = Board()
    # Default position
    assert(board.x == 0)
    assert(board.y == 0)
    assert(board.out_of_bounds() is False)
    # Right side
    board.x = 200
    assert(board.out_of_bounds() is False)
    board.x = 201
    assert(board.out_of_bounds())
    board.x = 200.1
    assert(board.out_of_bounds())
    # Left side
    board.x = -200
    assert(board.out_of_bounds() is False)
    board.x = -201
    assert(board.out_of_bounds())
    board.x = -200.1
    assert(board.out_of_bounds())
    # Top
    board.x = 0
    board.y = 200
    assert(board.out_of_bounds() is False)
    board.y = 201
    assert(board.out_of_bounds())
    board.y = 200.1
    assert(board.out_of_bounds())
    # Bottom
    board.y = -200
    assert(board.out_of_bounds() is False)
    board.y = -201
    assert(board.out_of_bounds())
    board.y = -200.1
    assert(board.out_of_bounds())
    # Bottom left corner
    board.x = -200
    board.y = -200
    assert(board.out_of_bounds() is False)
    board.x = -201
    assert(board.out_of_bounds())
    board.x = -200.1
    assert(board.out_of_bounds())
    board.x = -200
    board.y = -201
    assert(board.out_of_bounds())
    board.y = -200.1
    assert(board.out_of_bounds())
    # Bottom right corner
    board.x = 200
    board.y = -200
    assert(board.out_of_bounds() is False)
    board.x = 201
    assert(board.out_of_bounds())
    board.x = 200.1
    assert(board.out_of_bounds())
    board.x = 200
    board.y = -201
    assert(board.out_of_bounds())
    board.y = -200.1
    assert(board.out_of_bounds())
    # Upper left corner
    board.x = -200
    board.y = 200
    assert(board.out_of_bounds() is False)
    board.x = -201
    assert(board.out_of_bounds())
    board.x = -200.1
    assert(board.out_of_bounds())
    board.x = -200
    board.y = 201
    assert(board.out_of_bounds())
    board.y = 200.1
    assert(board.out_of_bounds())
    # Upper right corner
    board.x = 200
    board.y = 200
    assert(board.out_of_bounds() is False)
    board.x = 201
    assert(board.out_of_bounds())
    board.x = 200.1
    assert(board.out_of_bounds())
    board.x = 200
    board.y = 201
    assert(board.out_of_bounds())
    board.y = 200.1
    assert(board.out_of_bounds())


def test_click_to_row():
    board = Board()
    assert(board.y == 0)
    with pytest.raises(AttributeError):
        board.clicked_row is None
    board.click_to_row()
    assert(board.clicked_row == 4)
    board.y = -200.1
    board.click_to_row()
    assert(board.clicked_row == -1)
    board.y = -200
    board.click_to_row()
    assert(board.clicked_row == 0)
    board.y = -175
    board.click_to_row()
    assert(board.clicked_row == 0)
    board.y = -150
    board.click_to_row()
    assert(board.clicked_row == 1)
    board.y = -125
    board.click_to_row()
    assert(board.clicked_row == 1)
    board.y = -100
    board.click_to_row()
    assert(board.clicked_row == 2)
    board.y = -75
    board.click_to_row()
    assert(board.clicked_row == 2)
    board.y = -50
    board.click_to_row()
    assert(board.clicked_row == 3)
    board.y = -25
    board.click_to_row()
    assert(board.clicked_row == 3)
    board.y = 0
    board.click_to_row()
    assert(board.clicked_row == 4)
    board.y = 25
    board.click_to_row()
    assert(board.clicked_row == 4)
    board.y = 50
    board.click_to_row()
    assert(board.clicked_row == 5)
    board.y = 75
    board.click_to_row()
    assert(board.clicked_row == 5)
    board.y = 100
    board.click_to_row()
    assert(board.clicked_row == 6)
    board.y = 125
    board.click_to_row()
    assert(board.clicked_row == 6)
    board.y = 150
    board.click_to_row()
    assert(board.clicked_row == 7)
    board.y = 175
    board.click_to_row()
    assert(board.clicked_row == 7)
    board.y = 200
    board.click_to_row()
    assert(board.clicked_row == 8)
    board.y = 200.1
    board.click_to_row()
    assert(board.clicked_row == 8)


def test_click_to_col():
    board = Board()
    assert(board.x == 0)
    with pytest.raises(AttributeError):
        board.clicked_col is None
    board.click_to_col()
    assert(board.clicked_col == 4)
    board.x = -200.1
    board.click_to_col()
    assert(board.clicked_col == -1)
    board.x = -200
    board.click_to_col()
    assert(board.clicked_col == 0)
    board.x = -175
    board.click_to_col()
    assert(board.clicked_col == 0)
    board.x = -150
    board.click_to_col()
    assert(board.clicked_col == 1)
    board.x = -125
    board.click_to_col()
    assert(board.clicked_col == 1)
    board.x = -100
    board.click_to_col()
    assert(board.clicked_col == 2)
    board.x = -75
    board.click_to_col()
    assert(board.clicked_col == 2)
    board.x = -50
    board.click_to_col()
    assert(board.clicked_col == 3)
    board.x = -25
    board.click_to_col()
    assert(board.clicked_col == 3)
    board.x = 0
    board.click_to_col()
    assert(board.clicked_col == 4)
    board.x = 25
    board.click_to_col()
    assert(board.clicked_col == 4)
    board.x = 50
    board.click_to_col()
    assert(board.clicked_col == 5)
    board.x = 75
    board.click_to_col()
    assert(board.clicked_col == 5)
    board.x = 100
    board.click_to_col()
    assert(board.clicked_col == 6)
    board.x = 125
    board.click_to_col()
    assert(board.clicked_col == 6)
    board.x = 150
    board.click_to_col()
    assert(board.clicked_col == 7)
    board.x = 175
    board.click_to_col()
    assert(board.clicked_col == 7)
    board.x = 200
    board.click_to_col()
    assert(board.clicked_col == 8)
    board.x = 200.1
    board.click_to_col()
    assert(board.clicked_col == 8)


def test_is_player_square():
    board = Board()
    # Black
    board.clicked_row = 0
    board.clicked_col = 0
    assert(board.is_player_square(BLACK) is False)
    board.clicked_col = 7
    assert(board.is_player_square(BLACK))
    board.clicked_col = 3
    assert(board.is_player_square(BLACK))
    board.clicked_col = 4
    assert(board.is_player_square(BLACK) is False)
    board.clicked_col = 3.5
    with pytest.raises(TypeError):
        assert(board.is_player_square(BLACK))
    board.clicked_row = 1
    board.clicked_col = 0
    assert(board.is_player_square(BLACK))
    board.clicked_col = 7
    assert(board.is_player_square(BLACK) is False)
    board.clicked_col = 3
    assert(board.is_player_square(BLACK) is False)
    board.clicked_col = 4
    assert(board.is_player_square(BLACK))
    board.clicked_row = 2
    board.clicked_col = 0
    assert(board.is_player_square(BLACK) is False)
    board.clicked_col = 7
    assert(board.is_player_square(BLACK))
    board.clicked_col = 3
    assert(board.is_player_square(BLACK))
    board.clicked_col = 4
    assert(board.is_player_square(BLACK) is False)
    # Red
    board.clicked_row = 7
    board.clicked_col = 0
    assert(board.is_player_square(RED))
    board.clicked_col = 7
    assert(board.is_player_square(RED) is False)
    board.clicked_col = 3
    assert(board.is_player_square(RED) is False)
    board.clicked_col = 4
    assert(board.is_player_square(RED))
    board.clicked_row = 6
    board.clicked_col = 0
    assert(board.is_player_square(RED) is False)
    board.clicked_col = 7
    assert(board.is_player_square(RED))
    board.clicked_col = 3
    assert(board.is_player_square(RED))
    board.clicked_col = 4
    assert(board.is_player_square(RED) is False)
    board.clicked_row = 5
    board.clicked_col = 0
    assert(board.is_player_square(RED))
    board.clicked_col = 7
    assert(board.is_player_square(RED) is False)
    board.clicked_col = 3
    assert(board.is_player_square(RED) is False)
    board.clicked_col = 4
    assert(board.is_player_square(RED))


def test_is_movable_piece():
    pass


def test_valid_move():
    pass


def test_move_piece():
    pass


def test_ai_move():
    pass


def test_movable_pieces():
    pass


def test_move_count():
    pass
