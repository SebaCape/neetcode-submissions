class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_sum = 0
        max_sum = 0
        cur_sum1, cur_sum2 = 0, 0
        arr_sum = sum(nums)

        for n in nums:
            cur_sum1 += n
            cur_sum2 += n
            min_sum = min(cur_sum1, min_sum)
            max_sum = max(cur_sum2, max_sum)
            if cur_sum1 > 0:
                cur_sum1 = 0
            if cur_sum2 < 0:
                cur_sum2 = 0

        print(min_sum, max_sum, arr_sum)

        return max(arr_sum - min_sum, max_sum) if max_sum != 0 else max(nums)