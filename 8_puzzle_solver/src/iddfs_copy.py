def iddfs_copy(root, max_depth):
    for depth in range(max_depth):
        result = dfs_copy(root, depth)
        if result:
            return result
    return None

def dfs_copy(node, depth):
    if depth == 0:
        if node.is_goal():
            return node
        return None
    if depth > 0:
        for move in node.possible_moves():
            new_state = node.apply_move(move)
            result = dfs_copy(new_state, depth - 1)
            if result:
                return result
    return None
