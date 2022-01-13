def flood_fill_dfs(mat, x, y, rep):

    # flood fill algo fills the target val at x,y and all nearby target val to replacement val
    # it can use dfs or bfs traversal

    # possible movements
    ROW = (0, 0, 1, -1)
    COL = (1, -1, 0, 0)

    # get target val
    targ = mat[x][y]

    # invalid cases
    if not mat or not len(mat) or targ == rep:
        return

    stack = [(x, y)]

    # run dfs traversal to replace vals
    while stack:
        # get cur pos
        i, j = stack.pop()
        mat[i][j] = rep

        # add possible movements from cur pos
        for k in range(4):
            next_x = i + ROW[k]
            next_y = j + COL[k]

            # only add if movement valid and is target val
            if is_valid(mat, next_x, next_y) and mat[next_x][next_y] == targ:
                stack.append((next_x, next_y))


def flood_fill_bfs(mat, x, y, rep):

    # possible movements
    ROW = (0, 0, 1, -1)
    COL = (1, -1, 0, 0)

    # get target val
    targ = mat[x][y]

    # invalid cases
    if not mat or not len(mat) or not is_valid(mat, x, y) or targ == rep:
        return

    queue = [(x, y)]

    # run bfs traversal to replace vals
    while queue:
        # get cur pos
        i, j = queue.pop(0)
        mat[i][j] = rep

        # add possible movements from cur pos
        for k in range(4):
            next_x = i + ROW[k]
            next_y = j + COL[k]

            # only add if movement valid and is target val
            if is_valid(mat, next_x, next_y) and mat[next_x][next_y] == targ:
                queue.append((next_x, next_y))


# check if pos valid
def is_valid(mat, x, y):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0])


# mat = [
#     ["Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G"],
#     ["Y", "Y", "Y", "Y", "Y", "Y", "G", "X", "X", "X"],
#     ["G", "G", "G", "G", "G", "G", "G", "X", "X", "X"],
#     ["W", "W", "W", "W", "W", "G", "G", "G", "G", "X"],
#     ["W", "R", "R", "R", "R", "R", "G", "X", "X", "X"],
#     ["W", "W", "W", "R", "R", "G", "G", "X", "X", "X"],
#     ["W", "B", "W", "R", "R", "R", "R", "R", "R", "X"],
#     ["W", "B", "B", "B", "B", "R", "R", "X", "X", "X"],
#     ["W", "B", "B", "X", "B", "B", "B", "B", "X", "X"],
#     ["W", "B", "B", "X", "X", "X", "X", "X", "X", "X"],
# ]

# mat2 = [
#     ["Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G"],
#     ["Y", "Y", "Y", "Y", "Y", "Y", "G", "X", "X", "X"],
#     ["G", "G", "G", "G", "G", "G", "G", "X", "X", "X"],
#     ["W", "W", "W", "W", "W", "G", "G", "G", "G", "X"],
#     ["W", "R", "R", "R", "R", "R", "G", "X", "X", "X"],
#     ["W", "W", "W", "R", "R", "G", "G", "X", "X", "X"],
#     ["W", "B", "W", "R", "R", "R", "R", "R", "R", "X"],
#     ["W", "B", "B", "B", "B", "R", "R", "X", "X", "X"],
#     ["W", "B", "B", "X", "B", "B", "B", "B", "X", "X"],
#     ["W", "B", "B", "X", "X", "X", "X", "X", "X", "X"],
# ]

# x = 3
# y = 9

# replacement = "C"

# flood_fill_dfs(mat, x, y, replacement)
# flood_fill_bfs(mat2, x, y, replacement)

# for arr in mat:
#     print(arr)
