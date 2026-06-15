class Solution {
public:
    bool isPalindrome(string s)
    {
        int l{}, r = s.length() - 1;

        while(l < r)
        {
            while(!isalnum(s[l]) && l < r)
                l++;
            while(!isalnum(s[r]) && r > l)
                r--;

            if(tolower(s[l]) != tolower(s[r]))
                return false;
            else
            {
                l++;
                r--;
            }
        }
        return true;
    }
};