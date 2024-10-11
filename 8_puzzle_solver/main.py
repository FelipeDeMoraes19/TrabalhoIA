from src.puzzle import PuzzleState
from src.performance import compare_performance

if __name__ == "__main__":
    initial_board = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
    initial_state = PuzzleState(initial_board, (1, 1))
    
    compare_performance(initial_state, 10)
