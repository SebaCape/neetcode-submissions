
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#Must be able to divide cards into groups to get a valid answer
        n = len(hand)
        if n % groupSize != 0:
            return False

        #Count occurrences in our hand, make a sorted array of our keys (hand values)
        freq = defaultdict(int)
        for v in hand:
            freq[v] += 1
        vals = list(sorted(freq.keys()))
        

        #Go through each of our values and decrement consecutive occurences accordingly
        #(This can be done greedily in order because we always know we are starting from the smallest card in our group)
        for val in vals:
            for g in range(1, groupSize):
                freq[val + g] -= freq[val]
            freq[val] = 0

        #Verify based on mutated frequency map (all zeroes means divisibility is possible)
        s = set(freq.values())
        return 0 in s and len(s) == 1