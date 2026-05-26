class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []
        n = len(s)

        def backtrack(i):
            if i == n:
                for w in sol:
                    if w != w[::-1]:
                        return
                res.append(sol[:])
                return

            #Add to current existing substring:
            if sol:
                temp = sol[-1]
                sol[-1] += s[i]
                backtrack(i + 1)
                sol[-1] = temp

            #Create new substring partition:
            sol.append(s[i])
            backtrack(i + 1)
            sol.pop()
        
        backtrack(0)
        return res