class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #initialize variables and distance list for dijkstra's
        adj_list = defaultdict(list)
        dist = [float('inf')] * n

        #populate adjacency list with node edges with weight
        for src, dst, t in times:
            adj_list[src].append((dst, t))

        #initialize bfs priority queue with node dist and node
        min_heap = [(0, k)]
        dist[k - 1] = 0

        #traverse and assign weights to minimal network reach time
        while min_heap:
            cur_dist, cur_node = heapq.heappop(min_heap)

            #ignore inefficient distances
            if cur_dist > dist[cur_node - 1]:
                continue

            for node, time in adj_list[cur_node]:
                if dist[node - 1] > dist[cur_node - 1] + time:
                    dist[node - 1] = dist[cur_node - 1] + time
                    heapq.heappush(min_heap, (dist[node - 1], node))

        return -1 if max(dist) == float('inf') else max(dist)