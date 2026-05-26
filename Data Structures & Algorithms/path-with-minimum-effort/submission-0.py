class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]] # diff, row, col
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        #Always pick our path off the min heap to find the minimum difference to the destination
        while minHeap:
            diff, r, c = heapq.heappop(minHeap) #Take our current difference, row and column
            
            if (r, c) in visit: #If we hav seen this coordinate, skip
                continue

            visit.add((r, c))

            #If we are at the destination, return our maximum height difference in the minimum path
            if (r, c) == (ROWS - 1, COLS - 1): 
                return diff

            #Check every adjacent graph direction, and append the max difference on the given path
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (newR < 0 or newC < 0 or newR == ROWS or newC == COLS or (newR, newC) in visit):
                    continue
                newDiff = max(abs(heights[r][c] - heights[newR][newC]), diff)
                heapq.heappush(minHeap, [newDiff, newR, newC])
                