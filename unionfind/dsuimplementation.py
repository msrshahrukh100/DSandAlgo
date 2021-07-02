
m = "according to question constraints"


class DSU:

    def __init__(self):
        self.parent = [i for i in range(m)]
        self.rank = [0 for i in range(m)]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])

        return self.parent[u]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)

        if xr == yr:
            return False

        if self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr

        elif self.rank[yr] > self.rank[xr]:
            self.parent[xr] = yr

        else:
            self.parent[xr] = yr
            self.rank[yr] += 1

        return True


d = DSU(10)
