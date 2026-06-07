class Solution:
    def romanToInt(self, s: str) -> int:
        #Mapping from integer symbols to values
        val_map = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        #Return value
        num = 0

        #Keep running count of values, will always be monotonic lest a smaller prefix exists
        for i in range(len(s)):
            if i < len(s) - 1 and val_map[s[i]] < val_map[s[i + 1]]:
                num -= val_map[s[i]]
            else:
                num += val_map[s[i]]

        return num