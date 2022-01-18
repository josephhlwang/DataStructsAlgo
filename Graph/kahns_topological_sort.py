from graph import Graph

# a real life example would be package dependencies, if A > C and B > C, we would need to install A and B before
# thus sorting a graph with many dependencies topologically would give us an install order


def kahns_topological_sort(graph):

    # kahns topological sort uses an indegree arr to determine which vertices comes first
    # by bfs traversing through a list of indegree 0 vertices and removing all outgoing edges for each vertex
    # we can add new vertices to the indegree 0 queue after each edge is removed

    n = graph.size
    # get edges and indegree arr
    edges = graph.get_edges()
    in_deg = get_indeg(edges, n)

    # init sorted vert arr and no incoming edges arr
    sorted_vert = []
    no_incoming = []

    for vertex_id in graph.get_vertices():
        # queue all vertices with no incoming edges
        if in_deg[vertex_id] == 0:
            no_incoming.append(vertex_id)

    # for each edge with no incoming edges
    while no_incoming:

        cur_vertex_id = no_incoming.pop(0)
        # add it to sorted verts
        sorted_vert.append(cur_vertex_id)

        # for each edge of current vertex
        for u, v, _ in edges:
            if u == cur_vertex_id:
                # remove the outgoing edge to v
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    # if outgoing vertex has no more incoming edges, add it to queue
                    no_incoming.append(v)

    # since graph removes all incoming edges before queuing a vertex
    # a graph with a cycle has vertices with edges that cannot be removed
    # these edges are self dependent
    for i in range(n):
        if in_deg[i]:
            print("Graph contains cycle.")
            return []

    return sorted_vert


# create indegree arr so get indegree can be O(1)
def get_indeg(edges, n):
    in_deg = [0] * n

    for _, v, _ in edges:
        in_deg[v] += 1

    return in_deg


g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
g.add_vertex(7)
g.add_edge(0, 6, 0)
g.add_edge(1, 2, 0)
g.add_edge(1, 4, 0)
g.add_edge(1, 6, 0)
g.add_edge(3, 0, 0)
g.add_edge(3, 4, 0)
g.add_edge(5, 1, 0)
g.add_edge(7, 0, 0)
g.add_edge(7, 1, 0)
print(kahns_topological_sort(g))
