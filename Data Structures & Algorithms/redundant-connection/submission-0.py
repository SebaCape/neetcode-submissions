class DSU:
    def __init__(self, N):
        self.N = N
        self.size = [1] * N
        self.representative = list(range(N))

    def find(self, node):
        if self.representative[node] == node:
            return node
        self.representative[node] = self.find(self.representative[node])
        return self.representative[node]

    def union(self, n1, n2):
        n1 = self.find(n1)
        n2 = self.find(n2)

        if n1 == n2:
            return False
        else:
            if self.size[n1] > self.size[n2]:
                self.representative[n2] = n1
                self.size[n1] = self.size[n2]
            else: 
                self.representative[n1] = n2
                self.size[n2] = self.size[n1]
            return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)

        for n1, n2 in edges:
            if not dsu.union(n1 - 1, n2 - 1):
                return [n1, n2]

        return []