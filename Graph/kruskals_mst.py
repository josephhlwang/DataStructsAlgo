from graph import Graph
from DisjointSet.disjoint_set import DisjointSet


def kruskals(graph: Graph):
    # find and sort edges of graph
    edges = graph.get_edges()
    edges.sort(key=lambda x: x[2])

    n = graph.size
    # map subtrees as individual sets in disjoint set
    ds = DisjointSet(n)

    i = 0
    mst = []

    # for each edge of ascending weight
    while len(mst) < n - 1:

        (u, v, weight) = edges[i]
        # find roots of u,v
        x = ds.find_root(u)
        y = ds.find_root(v)

        # if roots are the same, they are connected within the same subtree
        # thus adding edge will create a cycle
        if x != y:
            # u,v in different subtrees, add edge and update roots
            mst.append([u, v, weight])
            ds.union(u, v)

        i += 1

    return mst


# g = Graph()
# g.add_vertex(0)
# g.add_vertex(1)
# g.add_vertex(2)
# g.add_vertex(3)
# g.add_vertex(4)
# g.add_vertex(5)
# g.add_vertex(6)
# g.add_edge(0, 1, 7)
# g.add_edge(0, 3, 5)
# g.add_edge(1, 2, 8)
# g.add_edge(1, 3, 9)
# g.add_edge(1, 4, 7)
# g.add_edge(2, 4, 5)
# g.add_edge(3, 4, 5)
# g.add_edge(3, 5, 6)
# g.add_edge(4, 5, 8)
# g.add_edge(4, 6, 9)
# print(g)
# print(kruskals(g))
