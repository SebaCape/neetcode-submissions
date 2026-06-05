class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        #Keep a count tracking pending decisions (+ is radiant - is dire)
        ct = 0
        senate = [ch for ch in senate]

        #Loop through string continuously and simulate senate until ct == length
        for c in senate:
            if c == 'R':
                if ct < 0:
                    senate.append('D')
                ct += 1
            else:
                if ct > 0:
                    senate.append('R')
                ct -= 1

        return "Radiant" if ct > 0 else "Dire"
                