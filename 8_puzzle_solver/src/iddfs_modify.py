import copy


def iddfs_modify(root, max_depth):
    for depth in range(max_depth):
        result = dfs_modify(root, depth)
        if result:
            return result
    return None

def dfs_modify(node, depth):
    if depth == 0:
        if node.is_goal():
            return node
        return None
    if depth > 0:
        x, y = node.empty_pos
        for move in node.possible_moves():
            prev_board = copy.deepcopy(node.board)  
            prev_empty = node.empty_pos
            
            node.apply_move(move)
            result = dfs_modify(node, depth - 1)
            
            if result:
                return result
            
            node.board = prev_board
            node.empty_pos = prev_empty
    return None
