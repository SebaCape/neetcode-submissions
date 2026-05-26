class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        
        #length must match
        if len(s3) != m + n:
            return False
        
        #dp[i][j] = True means s3[0:i+j] can be formed using s1[0:j] and s2[0:i] (boolean, not which string matches)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        
        # Base case: empty strings can form empty s3
        dp[0][0] = True
        
        #Initialize first column (using only s2)
        for i in range(1, n + 1):
            dp[i][0] = dp[i-1][0] and s2[i-1] == s3[i-1]
        
        #Initialize first row (using only s1)
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j-1] and s1[j-1] == s3[j-1]
        
        #Fill rest of DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                #Check reachability from either direction
                from_s2 = dp[i-1][j] and s2[i-1] == s3[i+j-1]
                from_s1 = dp[i][j-1] and s1[j-1] == s3[i+j-1]
                dp[i][j] = from_s2 or from_s1
        
        return dp[n][m]