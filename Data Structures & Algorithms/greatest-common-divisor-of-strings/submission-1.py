class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #Check if strings are valid for divisor comparison
        if str1 + str2 != str2 + str1:
            return ""

        #Apply euclids and return
        return str1[:math.gcd(len(str1), len(str2))]
