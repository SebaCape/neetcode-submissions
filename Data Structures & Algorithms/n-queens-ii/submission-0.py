class Solution:
    def totalNQueens(self, n: int) -> int:
        '''
            Queens can touch eachother if:
            1. They share the same column or row
            2. They share the same diagonal
        '''

        #Initialize our chessboard, result, and our coordinate sets
        res = 0
        chessboard = [['.'] * n for _ in range(n)]
        cols, p_diag, n_diag = set(), set(), set()

        def backtrack(r):
            nonlocal res
            #Terminate (succeding case)
            if r == n:
                res += 1
                return

            #Loop through all columns and backtrack
            for c in range(n):
                #Prune failing cases
                if c in cols or r + c in p_diag or r - c in n_diag:
                    continue

                #Recursively backtrack all possible row placements
                chessboard[r][c] = 'Q'
                cols.add(c)
                p_diag.add(r + c)
                n_diag.add(r - c)
                backtrack(r + 1)
                chessboard[r][c] = '.'
                cols.remove(c)
                p_diag.remove(r + c)
                n_diag.remove(r - c)

        backtrack(0)
        return res