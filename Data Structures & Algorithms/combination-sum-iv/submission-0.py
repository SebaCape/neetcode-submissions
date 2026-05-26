class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #Create a dp array holding possible ways to create sums at each index
        dp = [0] * (target + 1)
        dp[0] = 1

        #Check each value from the bottom up
        for i in range(len(dp)):
            #Check every number in our nums
            for j in range(len(nums)):
                #Combine smaller combinations at each dp index for every possible sum candidate
                if i - nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]

        return dp[-1] if dp[-1] != -1 else 0

