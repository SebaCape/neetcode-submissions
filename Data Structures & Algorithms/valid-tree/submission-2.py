class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        seen = set()
        node_to_edges = defaultdict(list)

        for n1, n2 in edges:
            node_to_edges[n1].append(n2)
            node_to_edges[n2].append(n1)

        def dfs(root):
            if root in seen:
                return 

            seen.add(root)

            for node in node_to_edges[root]:
                dfs(node)

        dfs(0)
        return len(seen) == n