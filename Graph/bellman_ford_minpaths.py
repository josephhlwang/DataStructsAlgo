from graph import Graph


def bellman_ford(graph: Graph, source_key):

    # the bellman ford algo dynamically finds the shortest dists from the source vertex every other vertex
    # it finds the shortest paths starting from the source vertex of length 1 to n-1
    # it can detect cycles by seeing if the min dists are updated after a nth iteration
    # this is because only a negative cycle can update the min dists

    n = graph.size
    edges = graph.get_edges()

    # min dist from source vertex
    min_dist = [float("inf")] * n
    # path tracker
    parent = [-1] * n
    # init self dist
    min_dist[source_key] = 0

    for i in range(n - 1):
        # for each dist from source to v
        for (u, v, w) in edges:
            # update min dist if taking u is faster
            if min_dist[u] != float("inf") and min_dist[u] + w < min_dist[v]:
                min_dist[v] = min_dist[u] + w
                parent[v] = u

    for (u, v, w) in edges:
        if min_dist[u] != float("inf") and min_dist[u] + w < min_dist[v]:
            # since dist is updated, there exists a negative cycle
            print("Graph contains negative weight cycle.")
            return

    for i in range(n):
        if i != source_key and min_dist[i] < float("inf"):
            print(
                f"The distance of vertex {i} from vertex {source_key} is {min_dist[i]}. "
                f"Its path is",
                getPath(parent, i),
            )


def getPath(parent, vertex):
    if vertex < 0:
        return []
    return getPath(parent, parent[vertex]) + [vertex]


# g = Graph()
# g.add_vertex(0)
# g.add_vertex(1)
# g.add_vertex(2)
# g.add_vertex(3)
# g.add_vertex(4)
# g.add_edge(0, 1, -1)
# g.add_edge(0, 2, 4)
# g.add_edge(1, 2, 3)
# g.add_edge(1, 3, 2)
# g.add_edge(1, 4, 2)
# g.add_edge(3, 2, 5)
# g.add_edge(3, 1, 1)
# g.add_edge(4, 3, -3)
# bellman_ford(g, 0)
# print(g)
