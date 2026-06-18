class Solution {
public:
    int climbStairs(int n) 
    {
        //Initialize dp states for the base cases, being the first and second steps
        int stair_dp_one{1};
        int stair_dp_two{2};
        int count = {2}; //Stair count/index
        int temp{};

        //Base case return value
        if(n < 3)
            return n == 1 ? 1 : 2;

        while(count < n)
        {
            //Calculate ways to reach this current step, update the last two steps accordingly, increment count
            temp = stair_dp_one;
            stair_dp_one = stair_dp_two;
            stair_dp_two += temp;
            count++;
        }

        //Final state will be stored at dp2 which is our last step
        return stair_dp_two;
    }
};
