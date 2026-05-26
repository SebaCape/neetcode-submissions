class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        import copy

        INF = 2147483647
        curq, nexq = deque([]), deque([])

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 0:
                    seen = set()
                    nexq.append((m + 1, n))
                    nexq.append((m - 1, n))
                    nexq.append((m, n + 1))
                    nexq.append((m, n - 1))
                    dist = 1
                    while nexq:
                        curq = copy.deepcopy(nexq)
                        nexq.clear()
                        while curq:
                            coords = curq.popleft()
                            if coords[0] < 0 or coords[1] < 0 or coords[0] >= len(grid) or coords[1] >= len(grid[0]) or coords in seen or grid[coords[0]][coords[1]] == -1:
                                continue
                            seen.add(coords)
                            grid[coords[0]][coords[1]] = min(grid[coords[0]][coords[1]], dist)
                            nexq.append((coords[0] + 1, coords[1]))
                            nexq.append((coords[0] - 1, coords[1]))
                            nexq.append((coords[0], coords[1] + 1))
                            nexq.append((coords[0], coords[1] - 1))
                        dist += 1



