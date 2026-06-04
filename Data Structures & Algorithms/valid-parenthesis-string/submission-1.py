class Solution:
    def checkValidString(self, s: str) -> bool:
        #Keep track of the minimum and maximum possible left parentheses remaining
        lmin, lmax = 0, 0

        for c in s:
            #Keep running count of min and max for left parentheses remaining
            if c == '(':
                lmin += 1
                lmax += 1
            #Wildcard can either be another left or right parenthetical, or it can be nothing
            elif c == '*':
                lmin -= 1
                lmax += 1
            else:
                lmin -= 1
                lmax -= 1
            
            #If our maximum remaining left parentheses is negative then we have an out of order right parenthetical and the string is invalid
            if lmax < 0:
                return False
            #We will never have less than one opening parenthetical
            if lmin < 0:
                lmin = 0

        #Check that no parentheticals remain
        return lmin == 0