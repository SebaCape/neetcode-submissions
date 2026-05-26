class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1

        queue = deque([("0000", 0)])
        visited = set("0000")

        while queue:
            combo, moves = queue.popleft()

            if combo == target:
                return moves

            for i in range(4):
                for direction in [-1, 1]:
                    new_digit = (int(combo[i]) + direction) % 10
                    new_combo = (combo[:i] + str(new_digit) + combo[i + 1:])

                    if new_combo not in visited and new_combo not in deadends:
                        visited.add(new_combo)
                        queue.append((new_combo, moves + 1))

        return -1