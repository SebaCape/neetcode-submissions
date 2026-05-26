class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        - Create a decision tree based on our possible word decisions

        - Navigate our tree, and truncate incorrect decision streams

        - Word pointer is updated after each navigation based on the length of our prior word decision length

        - Cache the possible decisions from different decision indices 
          (e.g. if i == 5 evaluates to a false path, save it in a dp array)
        '''
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s)) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
