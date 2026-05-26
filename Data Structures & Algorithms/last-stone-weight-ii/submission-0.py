class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #Initialize stone sum, and target value to reach for one of our two piles to smash
        stone_sum = sum(stones)
        target = stone_sum // 2
        n = len(stones)

        #Initialize dp table holding every stone from 1 to n, and whether it fits in our pile at some target value
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

        #Check every stone we have
        for idx in range(1, n + 1):
            #Check every known target size
            for t in range(target + 1):
                #If our stone fits within our current target size, we choose the maximum of skipping or including this stone
                if t >= stones[idx - 1]:
                    dp[idx][t] = max(dp[idx - 1][t], dp[idx - 1][t - stones[idx - 1]] + stones[idx - 1])
                #Otherwise, we just use our previous result
                else:
                    dp[idx][t] = dp[idx - 1][t]

        #The sum of our stones combined with the difference from removing our smallest stone pile twice is our solution
        return stone_sum - 2 * dp[n][target]