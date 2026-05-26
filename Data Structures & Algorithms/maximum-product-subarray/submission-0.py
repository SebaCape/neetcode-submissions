class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r_max, l_max = float('-inf'), float('-inf')
        multiplier = 1

        for n in nums:
            multiplier *= n
            if multiplier == 0:
                multiplier = 1
            else:
                l_max = max(multiplier, l_max)

        multiplier = 1

        for m in reversed(nums):
            multiplier *= m
            if multiplier == 0:
                multiplier = 1
            else:
                r_max = max(multiplier, r_max)

        return max([r_max, l_max, max(nums)])