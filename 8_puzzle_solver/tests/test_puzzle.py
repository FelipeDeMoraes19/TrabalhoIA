import pytest
from src.puzzle import PuzzleState

def test_is_goal():
    goal_state = PuzzleState([[1, 2, 3], [4, 5, 6], [7, 8, 0]], (2, 2))
    assert goal_state.is_goal()

def test_possible_moves():
    initial_state = PuzzleState([[1, 2, 3], [4, 0, 5], [7, 8, 6]], (1, 1))
    moves = initial_state.possible_moves()
    assert set(moves) == {"up", "down", "left", "right"}

def test_apply_move():
    initial_state = PuzzleState([[1, 2, 3], [4, 0, 5], [7, 8, 6]], (1, 1))

    new_state = initial_state.apply_move("right")
    assert new_state.board == [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
    assert new_state.empty_pos == (1, 2)

    new_state = new_state.apply_move("left")
    assert new_state.board == [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
    assert new_state.empty_pos == (1, 1)
