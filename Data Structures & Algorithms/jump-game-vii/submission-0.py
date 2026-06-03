class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        #Edge case for unreachability
        if s[-1] == '1':
            return False

        #DP array of traversability booleans
        n = len(s)
        dp = [False] * n
        dp[0] = True

        #Check entire string and populate dp array based on whether current index is reachable ('0')
        cnt = 0
        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                cnt += 1
            if i > maxJump and dp[i - maxJump - 1]:
                cnt -= 1
            if cnt > 0 and s[i] == '0':
                dp[i] = True

        #Return goal reachability
        return dp[-1]
