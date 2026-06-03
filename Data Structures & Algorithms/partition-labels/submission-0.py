class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #Var instantiation
        last_occ = {}
        res = []

        #Find last occurences of each character in string
        for i, c in enumerate(s):
            last_occ[c] = i

        #Loop through string keeping track of last occurrences to find partition
        start, end = 0, 0

        for j in range(len(s)):
            #If we find characters that end within our max range, they don't need to be considered
            end = max(end, last_occ[s[j]])
            if j == end:
                res.append(end - start + 1)
                start = j + 1

        return res
        