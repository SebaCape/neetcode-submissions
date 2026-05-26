class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        count = 0
        time = 0
        seen = set()

        #Add each rotten orange to queue and count unrotten oranges
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    count += 1
                elif grid[m][n] == 2:
                    count += 1
                    q.append((m, n))

        #Spread rot using BFS, count how much time needed for count to reach 0
        while q:
            for _ in range(len(q)):
                cur_loc = q.popleft()

                #Exit case at empty nodes or seen nodes or out of bounds nodes
                if cur_loc[0] < 0 or cur_loc[0] >= len(grid)  or cur_loc[1] < 0 or cur_loc[1] >= len(grid[0]) or grid[cur_loc[0]][cur_loc[1]] == 0 or cur_loc in seen:
                    continue

                seen.add(cur_loc)
                grid[cur_loc[0]][cur_loc[1]] = 2
                count -= 1

                #Add all adjacent nodes to queue
                q.append((cur_loc[0] + 1, cur_loc[1]))
                q.append((cur_loc[0] - 1, cur_loc[1]))
                q.append((cur_loc[0], cur_loc[1] + 1))
                q.append((cur_loc[0], cur_loc[1] - 1))
            time += 1

        return max(time - 2, 0) if count == 0 else -1