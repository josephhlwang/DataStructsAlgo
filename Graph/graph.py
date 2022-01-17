from Graph.vertex import Vertex


class Graph:
    def __init__(self):
        # Graph holds vertices in a dictionary, key:Vertex
        # The key, key, is the id of a vertex and the value, Vertex, is a Vertex object
        self.vertices = {}
        self.size = 0

    def get_vertices(self):
        return self.vertices.keys()

    def add_vertex(self, key):
        if key not in self:
            new = Vertex(key)
            self.vertices[key] = new
            self.size += 1
        else:
            print("Key already exists.")

    def add_edge(self, from_key, to_key, weight=0):
        if from_key in self and to_key in self:
            self.vertices[from_key].add_neighbour(self.vertices[to_key], weight)
        elif from_key in self:
            print("to_key does not exist.")
        else:
            print("from_key does not exist.")

    def remove_edge(self, from_key, to_key):
        if from_key in self and to_key in self:
            self.vertices[from_key].remove_neighbour(self.vertices[to_key])
        elif from_key in self:
            print("to_key does not exist.")
        else:
            print("from_key does not exist.")

    def remove_vertex(self, key):
        if key in self:
            for k in self.get_vertices():
                if k != key:
                    self.remove_edge(k, key)
            self.vertices.pop(key)
        else:
            print("Key does not exist.")

    def get_vertex(self, key):
        return self.vertices[key]

    def __contains__(self, key):
        return key in self.get_vertices()

    def __str__(self):
        s = ""
        for vertex_id in self.get_vertices():
            vertex = self.get_vertex(vertex_id)
            ids = " ".join([str(v) for v in vertex.get_neighbours()])
            if not ids:
                ids = "nothing"
            connected = f"{vertex} is connected to {ids}"
            s += connected + "\n"

        return s

    def bfs(self, start_key):
        if start_key in self:
            # bfs uses queue to traverse neighbours first
            queue = [self.get_vertex(start_key)]
            # use set to keep track of visited
            visited = set()

            while queue:
                cur = queue.pop(0)
                if cur not in visited:
                    print(cur.id)
                    visited.add(cur)

                    for nbr in cur.get_neighbours():
                        if nbr not in visited:
                            queue.append(nbr)

        else:
            print("start_key does not exist.")

    def dfs(self, start_key):
        if start_key in self:
            # dfs uses stack to traverse as far as possible first
            stack = [self.get_vertex(start_key)]
            # use set to keep track of visited
            visited = set()

            while stack:
                cur = stack.pop()
                if cur not in visited:
                    print(cur.id)
                    visited.add(cur)

                    for nbr in cur.get_neighbours():
                        if nbr not in visited:
                            stack.append(nbr)

        else:
            print("start_key does not exist.")

    def get_edges(self):
        verts = self.get_vertices()
        edges = []

        for key in verts:
            vert = self.get_vertex(key)
            for nbr in vert.get_neighbours():
                weight = vert.get_weight(nbr)
                edges.append([vert.id, nbr.id, weight])

        return edges

    def get_adj_matrix(self):
        edges = self.get_edges()
        n = self.size

        adj = [[-1] * n for i in range(n)]
        for edge in edges:
            (u, v, w) = edge
            adj[u][v] = w

        return adj


# g = Graph()
# g.add_vertex(0)
# g.add_vertex(1)
# g.add_vertex(2)
# g.add_vertex(3)
# g.add_vertex(4)
# g.add_vertex(5)
# g.add_vertex(6)
# g.add_vertex(7)
# g.add_edge(0, 2, 1)
# g.add_edge(0, 3, 1)
# g.add_edge(0, 4, 1)
# g.add_edge(1, 6, 1)
# g.add_edge(2, 0, 1)
# g.add_edge(2, 6, 1)
# g.add_edge(4, 2, 1)
# g.add_edge(4, 7, 1)
# g.add_edge(5, 6, 1)
# g.add_edge(5, 7, 1)
# g.add_edge(6, 5, 1)
# g.remove_vertex(2)
# print(g)
# g.dfs(0)
