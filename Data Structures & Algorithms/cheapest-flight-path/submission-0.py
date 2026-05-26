class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dists = [float('inf')] * n
        dists[src] = 0

        for i in range(k + 1):
            temp_dists = dists.copy()

            for source, destination, dist in flights:
                if dists[source] == float('inf'):
                    continue
                if dist + temp_dists[source] < dists[destination]:
                    dists[destination] = dist + temp_dists[source]

        return -1 if dists[dst] == float('inf') else dists[dst]