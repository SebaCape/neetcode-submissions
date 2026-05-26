class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = -1

        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if obstacleGrid[row][col] == 1 or (row == 0 and col == 0):
                    continue

                val = 0
                if row != 0 and obstacleGrid[row - 1][col] != 1:
                    val += obstacleGrid[row - 1][col]
                if col != 0 and obstacleGrid[row][col - 1] != 1: 
                    val += obstacleGrid[row][col - 1]

                obstacleGrid[row][col] = val

        return -obstacleGrid[-1][-1]