class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return

        # Union by rank
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

# Example usage:
dsu = DisjointSet(7)
dsu.union(0, 1)
dsu.union(1, 2)
dsu.union(3, 4)
dsu.union(5, 6)
dsu.union(4, 5)

# Check if 2 and 0 are connected
print("Connected (2, 0):", dsu.find(2) == dsu.find(0))  # True
print("Connected (2, 3):", dsu.find(2) == dsu.find(3))  # False
print("Connected (4, 6):", dsu.find(4) == dsu.find(6))  # True
