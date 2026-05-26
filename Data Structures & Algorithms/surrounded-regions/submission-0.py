class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #Create set for modified region alongside board bounds
        safe = set()
        rows, cols = len(board), len(board[0])

        #Create depth first search function for later use
        def dfs(m, n, visited):
            #terminate if out of bounds, not an O, or already visited
            if m < 0 or n < 0 or m >= rows or n >= cols or board[m][n] == 'X' or (m, n) in visited:
                return

            visited.add((m, n))
            
            dfs(m + 1, n, visited)
            dfs(m, n + 1, visited)
            dfs(m - 1, n, visited)
            dfs(m, n - 1, visited)
            
            return

        #DFS from each edge of our matrix
        for row in range(rows):
            if board[row][0] == 'O':
                dfs(row, 0, safe)
            if board[row][-1] == 'O':
                dfs(row, cols - 1, safe)

        for col in range(cols):
            if board[0][col] == 'O':
                dfs(0, col, safe)
            if board[-1][col] == 'O':
                dfs(rows - 1, col, safe)

        #Loop through matrix, set all surrounded values (values not in 'safe') to X
        for y in range(rows):
            for z in range(cols):
                if (y, z) not in safe:
                    board[y][z] = 'X'