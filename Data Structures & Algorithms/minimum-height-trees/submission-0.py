class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #Initialize an array to keep track of array heights + minimum height trees
        heights = [0] * n
        res = []

        #Adjacency list initialization
        adj_list = defaultdict(list)

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        #Conduct BFS from each node, and keep count of the amount of tree levels
        for node in range(n):
            q = deque([node])
            seen = set()
            height = -1
            while q:
                for _ in range(len(q)):
                    cur_node = q.popleft()
                    seen.add(cur_node)
                    for nxt in adj_list[cur_node]:
                        if nxt not in seen:
                            q.append(nxt)
                height += 1
            heights[node] = height

        #Find our minimum height, and append all BFS trees with that height to our result
        min_height = min(heights)

        for i, h in enumerate(heights):
            if h == min_height:
                res.append(i)

        return res