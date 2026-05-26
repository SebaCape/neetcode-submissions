class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dfs(i):
            #Already cached
            if i in dp:
                return dp[i]
            #No ways to decode string starting with zero
            if s[i] == '0':
                return 0

            #Check encoding of next index (do not join)
            res = dfs(i + 1)
            #Check if current index has valid encoding when joined with next one
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)
