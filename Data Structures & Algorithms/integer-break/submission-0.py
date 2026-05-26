class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1

        threes = n // 3
        twos = 0
        remainder = n % 3

        if remainder == 1:
            threes -= 1
            twos = 2
        if remainder == 0:
            remainder = 1

        return 3 ** threes * 2 ** twos * remainder