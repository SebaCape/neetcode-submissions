class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def backtrack(i, sol):
            if i == n:
                res.append(sol[:])
                return

            #All subsets with nums[i]
            sol.append(nums[i])
            backtrack(i + 1, sol)
            sol.pop() #Backtrack

            #All subsets without nums[i]
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, sol)

        backtrack(0, [])

        return res