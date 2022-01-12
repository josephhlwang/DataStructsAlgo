from Graph.graph import Graph

# floyd warshall algo uses dynamic programming to find shortest paths from all nodes to all nodes
# if mid dist matrix diag contains negative, then graph contains negative cycles


def floyd_warshall(graph):

    # init shortest distance adjacency matrix
    adj = graph.get_adj_matrix()
    n = graph.size
    min_dist = [[float("inf")] * n for i in range(n)]

    # set self distance to 0
    for i in range(n):
        min_dist[i][i] = 0

    # copy edges from graph adjacency matrix
    for i in range(n):
        for j in range(n):
            if adj[i][j] != -1:
                min_dist[i][j] = adj[i][j]

    # k is a pivot vertex
    # i and j are vertices we are trying to find the shortest path for

    # for each pivot
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d = min_dist[i][k] + min_dist[k][j]
                # if using that pivot is shorter than the edge
                if d < min_dist[i][j]:
                    # update the shortest dist for i,j
                    min_dist[i][j] = d

    # print results
    for i in range(n):
        for j in range(n):
            if i != j:
                d = min_dist[i][j]
                if d != float("inf"):
                    print(f"Min path from {i} to {j} is {d}")


g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
g.add_edge(0, 1, 7)
g.add_edge(0, 3, 5)
g.add_edge(1, 2, 8)
g.add_edge(1, 3, 9)
g.add_edge(1, 4, 7)
g.add_edge(2, 4, 5)
g.add_edge(3, 4, 5)
g.add_edge(3, 5, 6)
g.add_edge(4, 5, 8)
g.add_edge(4, 6, 9)
# print(g)
# print(g.get_edges())
# print(g.get_adj_matrix())
floyd_warshall(g)
