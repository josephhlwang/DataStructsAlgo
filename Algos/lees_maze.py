def lees_shortest_dist(mat, src, dest):

    # lees shortest dist algo finds the shortest distance from src to dest
    # it uses a bst traversal to find the shortest path
    # it tracks visited positions to speed up process

    # possible movements
    ROW = (0, 0, 1, -1)
    COL = (1, -1, 0, 0)

    i, j = src
    x, y = dest

    # invalid cases
    if not mat or not len(mat) or not is_valid(mat, i, j) or not is_valid(mat, x, y):
        return -1

    # mat to track visited elements
    visited = [[False for j in range(len(mat[0]))] for i in range(len(mat))]

    # in case dest not reachable
    min_dist = float("inf")

    visited[i][j] = True
    queue = [(i, j, 0)]

    # run bfs traversal to find shortest dist
    while queue:
        # get cur pos
        i, j, dist = queue.pop(0)
        if i == x and j == y:
            min_dist = dist
            break

        # add possible movements from cur pos
        for k in range(4):
            next_x = i + ROW[k]
            next_y = j + COL[k]

            # only add if movement valid and not visited
            if is_valid(mat, next_x, next_y) and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y, dist + 1))

    if min_dist == float("inf"):
        return -1

    return min_dist


# check if pos valid
def is_valid(mat, x, y):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == 1


# maze = [
#     [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
#     [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
#     [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
#     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
#     [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#     [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
#     [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
#     [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#     [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
#     [0, 0, 1, 0, 0, 1, 1, 0, 0, 1],
# ]

# src = (0, 0)
# dest = (7, 5)

# print(lees_shortest_dist(maze, src, dest))
