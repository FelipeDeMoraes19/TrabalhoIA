import pytest
from src.iddfs_copy import iddfs_copy
from src.puzzle import PuzzleState

def test_iddfs_copy_goal_found():
    goal_state = PuzzleState([[1, 2, 3], [4, 5, 6], [7, 8, 0]], (2, 2))
    result = iddfs_copy(goal_state, max_depth=5)
    assert result is not None  
    assert result.is_goal()

def test_iddfs_copy_no_solution():
    unsolvable_state = PuzzleState([[1, 2, 3], [4, 5, 6], [8, 7, 0]], (2, 2))  
    result = iddfs_copy(unsolvable_state, max_depth=5)
    assert result is None 
