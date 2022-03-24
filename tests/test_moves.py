'''
Jake Van Meter
CS5001 Fall 2021
Test file for Moves class.
'''
import pytest
from moves import Moves
from constants import DEFAULT_BOARD, BLACK, RED


def constructor():
    moves = Moves(BLACK, DEFAULT_BOARD)
    assert(moves.player == BLACK)
    assert(moves.board == DEFAULT_BOARD)
    assert(moves.available_moves == [])
    moves = Moves(RED, DEFAULT_BOARD)
    assert(moves.player == RED)
    assert(moves.board == DEFAULT_BOARD)
    assert(moves.available_moves == [])


def test_blk_reg():
    pass


def test_red_reg():
    pass


def test_king():
    pass


def test_force_capture():
    pass
