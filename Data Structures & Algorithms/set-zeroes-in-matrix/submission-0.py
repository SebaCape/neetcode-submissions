class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Mark rows and columns with zeroes
        marked_rows, marked_cols = set(), set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    marked_rows.add(i)
                    marked_cols.add(j)
        
        #Mutate matrix
        for row in range(m):
            for col in range(n):
                if row in marked_rows or col in marked_cols:
                    matrix[row][col] = 0