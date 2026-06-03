class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #Count occurrences in our hand
        freq = Counter(hand)

        #Greedily traverse in increasing order and decrement subsequent group candidates
        for i in sorted(freq):
            if freq[i] > 0:
                for j in range(groupSize - 1, 0, -1):
                    freq[i + j] -= freq[i]
                    #If at any point we create a negative candidate, then our cards can't be grouped as desired
                    if freq[i + j] < 0:
                        return False

        return True