class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        seen = set()

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        def dfs(node):
            if node in seen:
                return

            seen.add(node)

            for c in adj_list[node]:
                dfs(c)

        csum = 0
        for i in range(n):
            if i in seen:
                continue
            dfs(i)
            csum += 1

        return csum