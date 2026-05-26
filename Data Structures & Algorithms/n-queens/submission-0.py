class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
            Queens can touch eachother if:
            1. If they share an x or y coordinate
            2. If they share a diagonal (HARDEST CASE)
        '''

        #Initialize chessboard and store coordinates to check above parameters
        chessboard = [['.'] * n for _ in range(n)]
        res = []
        #Store queen columns, positive diagonals, and negative diagonals in set (col, row + col, row - col)
        cols, pos_diag, neg_diag = set(), set(), set() 

        #Define a function for current row and column + how many queens are left
        def backtrack(row):
            #Successful termination case
            if row == n:
                res.append([''.join(_) for _ in chessboard])
                return

            #Loop through every column to place a queen
            for col in range(n):
                #Failed termination case (prunes recursive branch)
                if row + col in pos_diag or col in cols or row - col in neg_diag:
                    continue

                #Backtrack and update sets accordingly
                chessboard[row][col] = 'Q'
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                backtrack(row + 1)
                chessboard[row][col] = '.'
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
        
        backtrack(0)
        return res
