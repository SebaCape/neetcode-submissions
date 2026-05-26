class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Populate adjacency list with points and edge lengths
        adj_list = defaultdict(list)

        for i in range(len(points)):
            for j in range(len(points)):
                if j == i:
                    continue
                adj_list[i].append(cur_edge := ((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])), j))
            adj_list[i].sort()

        #Create min-heap and seen set to perform Prim's algorithm
        min_heap = [(0, 0)]
        seen = set()
        cost = 0

        #Greedy BFS, ignore seen nodes, increment cost iteratively
        while min_heap:
            cur_cost, cur_node = heapq.heappop(min_heap)

            if cur_node in seen:
                continue

            cost += cur_cost
            seen.add(cur_node)

            for edge in adj_list[cur_node]:
                heapq.heappush(min_heap, edge)

        #Return our final minimum cost
        return cost

        
