class CountSquares:
    def __init__(self):
        self.pcount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pcount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point

        for x1, y1 in self.points:
            if (abs(y - y1) != abs(x - x1)) or x1 == x or y1 == y:
                continue
            res += self.pcount[(x1, y)] * self.pcount[(x, y1)]
        
        return res
