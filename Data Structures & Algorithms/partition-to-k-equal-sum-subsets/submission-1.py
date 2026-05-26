class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        target = sum(nums) // k

        nums.sort(reverse = True)
        res = [0] * k

        def backtrack(i):
            if i == len(nums):
                for n in res:
                    if n != target:
                        return False
                return True

            for l in range(k):
                if res[l] + nums[i] > target or (l > 0 and res[l] == res[l - 1]):
                    continue

                res[l] += nums[i]
                if backtrack(i + 1):
                    return True
                res[l] -= nums[i]

            return False

        return backtrack(0)

