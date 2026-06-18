class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) 
    {
        //Initialize hashmap to count letters in magazine
        unordered_map<char, int> letter_frequencies;

        for(char c : magazine)
            //[] operator will initialize a 0 value if the key does not exist
            letter_frequencies[c]++;

        //Count through our ransomNote now and if at any point we find a 0 value, we can exit
        for(char c : ransomNote)
        {
            //Decrement and value checking encoded within conditional
            if(!letter_frequencies[c]--)
                return false;
        }

        //Ransom note can be made if no scarcities found
        return true;
    }
};