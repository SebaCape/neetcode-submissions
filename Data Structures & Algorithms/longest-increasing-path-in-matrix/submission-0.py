class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #Create dp matrix to store longest paths from different sources
        m, n = len(matrix), len(matrix[0])
        paths_from_src = [[1 for _ in range(n)] for _ in range(m)]

        #Define recursive dfs function for path traversal
        def dfs(row, col):
            nonlocal paths_from_src
            adjacencies = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

            for r, c in adjacencies:
                if r >= 0 and r < m and c >= 0 and c < n and matrix[r][c] > matrix[row][col]:
                    paths_from_src[row][col] = max(paths_from_src[row][col], 1 + dfs(r, c) if paths_from_src[r][c] == 1 else 1 + paths_from_src[r][c])

            return paths_from_src[row][col]

        for i in range(m):
            for j in range(n):
                dfs(i, j)

        return max([max(v) for v in paths_from_src])