class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False

        target = sum(matchsticks) // 4
        res = [0, 0, 0, 0]
        matchsticks.sort(reverse = True)

        def backtrack(i):
            if i == len(matchsticks):
                return res[0] == res[1] == res[2] == target

            #Choose to include on each side and remove accordingly
            for k in range(4):
                #Skip equal buckets & target overflows
                if (k > 0 and res[k] == res[k - 1]) or res[k] + matchsticks[i] > target:
                    continue
                #Backtrack, return boolean so that truth value cascades upwards
                res[k] += matchsticks[i]
                if backtrack(i + 1):
                    return True
                res[k] -= matchsticks[i]

            #No dice
            return False

        return backtrack(0)