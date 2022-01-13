from graph import Graph
from PriorityQueue.binary_heap import BinaryHeap

# dijkstras finds the min dist from a source vertex to all other vertices
# it updates the shortest distance to neighbours from the min vertex of priority queue
def dijkstras(graph: Graph, source_key):
    n = graph.size
    source_vertex = graph.get_vertex(source_key)

    # keeps track of min dist from source vertex
    min_dist = [float("inf")] * n
    # keeps track of visited vertices
    done = [False] * n
    # keeps track of min path parent of each vertex
    prev = [-1] * n

    # init source values
    min_dist[source_key] = 0
    done[source_key] = True

    # use priority queue to track min vertex of avaliable vertices
    pq = BinaryHeap()
    pq.enqueue(0, source_vertex)

    while pq.size:
        cur_node = pq.dequeue()
        cur_vertex = cur_node.payload
        # dist from source node to current node
        dist_to_vertex = cur_node.val

        # for each neighbour of current node
        for nbr_vertex in cur_vertex.get_neighbours():
            dist_to_nbr = cur_vertex.get_weight(nbr_vertex)
            # calculate dist from current node to the neighbour
            d = dist_to_vertex + dist_to_nbr

            # if neighbour not visited
            # and if using current node as pivot to neighbour is cheaper than going straight from source node to neighbour
            if not done[nbr_vertex.id] and min_dist[nbr_vertex.id] > d:
                # update new min dist of source to neighbour
                min_dist[nbr_vertex.id] = d
                # queue neighbour
                pq.enqueue(d, nbr_vertex)
                # update path taken
                prev[nbr_vertex.id] = cur_vertex.id

        done[cur_vertex.id] = True

    route = []
    # for each vertex
    for i in range(n):
        # if min dist found
        if i != source_key and min_dist[i] != float("inf"):
            # get route
            get_route(prev, i, route)
            print(
                f"Path ({source_key} —> {i}): Minimum cost = {min_dist[i]}, Route = {route}"
            )
            route.clear()


def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)


# g = Graph()
# g.add_vertex(0)
# g.add_vertex(1)
# g.add_vertex(2)
# g.add_vertex(3)
# g.add_vertex(4)
# g.add_edge(0, 1, 3)
# g.add_edge(0, 2, 10)
# g.add_edge(1, 2, 1)
# g.add_edge(1, 3, 2)
# g.add_edge(1, 4, 8)
# g.add_edge(2, 1, 4)
# g.add_edge(2, 4, 2)
# g.add_edge(3, 4, 7)
# g.add_edge(4, 3, 9)
# dijkstras(g, 0)
# print(g)
