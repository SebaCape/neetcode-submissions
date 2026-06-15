class Solution {
public:
    int maxProfit(vector<int>& prices) 
    {
        //We want to keep track of the values that we can buy and sell at
        int buyVal = prices[0], sellVal = prices[0];
        int maxProfit = 0;

        //Check for monotonic sections and make a trade when they break
        for(int i = 1; i < prices.size(); i++)
        {
            if(buyVal >= prices[i])
            {
                buyVal = prices[i];
                sellVal = 0;
            }
            //Choose the best selling value if possible
            else if(sellVal < prices[i])
            {
                sellVal = prices[i];
            }
            maxProfit = max(sellVal - buyVal, maxProfit);
        }
        return maxProfit;
    }
};