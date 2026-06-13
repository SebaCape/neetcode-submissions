class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        //Initialize unordered map for element index pairs
        unordered_map<int, int> occ;

        //Loop through all of our numbers
        for(int i = 0; i < nums.size(); i++)
        {
            //Return our coordinate array when elements found
            if(occ.find(target - nums[i]) != occ.end())
                return {occ[target - nums[i]], i};

            //Add current element to our map with index
            occ[nums[i]] = i;
        }
        //Unreachable code block
        return {0, 0};
    }
};