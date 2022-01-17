class Vertex:
    def __init__(self, id):

        # Vertex uses an Adjacency List implementation which uses a dictionary, neighbour:weight
        # The key, neighbour, is a Vertex object and the value, weight, is a integer
        # AL better when there aren't many edges, uses less memory; AM better when there's no memory restriction and when O(1) edge lookup is required
        self.conneted_to = {}
        self.id = id

    def __str__(self):
        return str(self.id)

    def add_neighbour(self, nbr, weight=0):
        self.conneted_to[nbr] = weight

    def remove_neighbour(self, nbr):
        if nbr in self.conneted_to:
            self.conneted_to.pop(nbr)

    def get_neighbours(self):
        return self.conneted_to.keys()

    def get_weight(self, nbr):
        return self.conneted_to[nbr]


# v = Vertex(1)
# b = Vertex(2)
# n = Vertex(3)
# m = Vertex(4)

# v.add_neighbour(b, 1)
# v.add_neighbour(n, 2)
# v.add_neighbour(m, 3)

# print(v)
