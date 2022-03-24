'''
Jake Van Meter
CS5001 Fall 2021
Test file for GameState class.
'''
import pytest
from gamestate import GameState
from constants import BLACK, RED


def test_constructor():
    gs = GameState()
    assert(gs.current_player == BLACK)
    assert(gs.opposite_player == RED)
    assert(gs.piece_selected is False)
    assert(gs.ai_player is False)
    assert(gs.ai_player_color == RED)
    with pytest.raises(AttributeError):
        assert(gs.winner is None)


def test_swap_turn():
    gs = GameState()
    # Default values of the current_player and opposite_player attributes
    assert(gs.current_player == BLACK)
    assert(gs.opposite_player == RED)
    # After black's turn is over
    gs.swap_turn()
    assert(gs.current_player == RED)
    assert(gs.opposite_player == BLACK)
    # After red's turn is over
    gs.swap_turn()
    assert(gs.current_player == BLACK)
    assert(gs.opposite_player == RED)


def test_game_over():
    gs = GameState()
    with pytest.raises(AttributeError):
        assert(gs.winner is None)
    assert(gs.game_over(1, 1, 1, 1) is False)
    # When red runs out of pieces
    assert(gs.game_over(0, 1, 1, 1))
    assert(gs.winner == "Black")
    # When black runs out of pieces
    assert(gs.game_over(1, 0, 1, 1))
    assert(gs.winner == "Red")
    # When red runs out of moves
    assert(gs.game_over(1, 1, 0, 1))
    assert(gs.winner == "Black")
    # When black runs out of moves
    assert(gs.game_over(1, 1, 1, 0))
    assert(gs.winner == "Red")
