class Solution {
public:
    bool isValid(string s) 
    {
        //Initialize stack for bookkeeping
        vector<char> stack;

        //Loop through all characters
        for(char ch : s)
        {
            //If opening clause, add to stack
            if(ch == '(' || ch == '[' || ch == '{')
            {
                stack.push_back(ch);
            }
            //If closing clause, check if corresponding match exists
            else if(stack.size() != 0)
            {
                //Nested if statement to prevent segmentation fault
                if(ch == ')' ? stack.back() == ch - 1 : stack.back() == ch - 2)
                    stack.pop_back();
                else
                    return false;
            }
            //If we reach here, then we have an invalid closing clause, and we return false
            else
            {
                return false;
            }
        }

        

        //Iff all parentheses are consumed, then validity is proven
        return stack.size() == 0;
    }
};