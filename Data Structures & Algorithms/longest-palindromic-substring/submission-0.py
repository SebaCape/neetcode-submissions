class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_start = 0
        res_end = 0
        n = len(s)

        for i in range(n):
            #Odd palindromes
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > res_end:
                    res_start = l
                    res_end = r - l
                l -= 1
                r += 1
            
            #Even Palindromes
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > res_end:
                    res_start = l
                    res_end = r - l
                l -= 1
                r += 1

        return s[res_start:res_start + res_end + 1]
