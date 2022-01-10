class DisjointSet:

    # A class used to track disjoint sets
    # Each set has a root, which is the "label" of each set
    # Comparing two sets can be done by comparing their roots
    # Merging two sets can be done by setting the root of one set to the root of another set

    def __init__(self, n):
        self.parent = {}

        for i in range(n):
            # init n sets
            self.parent[i] = i

    def find_root(self, key):
        if self.parent[key] == key:
            return key

        # finds root of key recursively
        return self.find_root(self.parent[key])

    def union(self, u, v):
        # Merging two sets
        x = self.find_root(u)
        y = self.find_root(v)

        self.parent[x] = y
