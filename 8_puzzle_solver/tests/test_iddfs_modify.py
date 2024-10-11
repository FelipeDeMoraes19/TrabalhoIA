import pytest
from src.iddfs_modify import iddfs_modify
from src.puzzle import PuzzleState

def test_iddfs_modify_goal_found():
    goal_state = PuzzleState([[1, 2, 3], [4, 5, 6], [7, 8, 0]], (2, 2))
    result = iddfs_modify(goal_state, max_depth=5)
    assert result is not None 
    assert result.is_goal()

def test_iddfs_modify_no_solution():
    unsolvable_state = PuzzleState([[1, 2, 3], [4, 5, 6], [8, 7, 0]], (2, 2)) 
    result = iddfs_modify(unsolvable_state, max_depth=5)
    assert result is None 
