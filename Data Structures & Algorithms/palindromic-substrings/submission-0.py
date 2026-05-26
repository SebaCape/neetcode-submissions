class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        #Helper function to check all palindromes in a string from starting indices in O(N) time
        def pal_check(l, r, string):
            pal_count = 0

            while l >= 0 and r < n and string[l] == string[r]:
                pal_count += 1
                l -= 1
                r += 1

            return pal_count

        for i in range(n):
            #All odd substrings
            count += pal_check(i, i, s)

            #All even substrings
            count += pal_check(i, i + 1, s)

        return count