class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #Remove triplets with maximum values greater than target values (unusable)
        for i in range(len(triplets)):
            for j in range(3):
                if triplets[i][j] > target[j]:
                    triplets[i] = [-1, -1, -1]

        #Track all seen values at indices in our valid triplets
        aseen, bseen, cseen = set(), set(), set()
        for a, b, c in triplets:
            if a == -1:
                continue
            aseen.add(a)
            bseen.add(b)
            cseen.add(c)

        #See if the target can be formed
        return target[0] in aseen and target[1] in bseen and target[2] in cseen