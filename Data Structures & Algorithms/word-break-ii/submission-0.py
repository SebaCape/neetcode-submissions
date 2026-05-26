class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res, sol = [], []

        def backtrack(i):
            if i == len(s):
                res.append(" ".join(sol))
                return

            for j in range(i, len(s)):
                w = s[i: j + 1]
                if w in wordDict:
                    sol.append(w)
                    backtrack(j + 1)
                    sol.pop()

        backtrack(0)
        return res
