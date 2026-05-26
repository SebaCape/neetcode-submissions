class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])

        for idx in range(len(diff) - 1, -1, -1):
            diff[idx] += diff[(idx + 1) % len(diff)]

        print(diff)

        return diff.index(max(diff))