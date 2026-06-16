class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        //Two frequency maps, you know the drill
        unordered_map<char, int> s_map, t_map;

        for(int i{}; i < s.length(); i++)
        {
            if(s_map.contains(s[i]))
                s_map[s[i]] += 1;
            else
                s_map[s[i]] = 1;
        }

        for(int i{}; i < t.length(); i++)
        {
            if(t_map.contains(t[i]))
                t_map[t[i]] += 1;
            else
                t_map[t[i]] = 1;

            if(t_map[t[i]] > s_map[t[i]])
                return false;
        }

        return s_map == t_map;
    }
};