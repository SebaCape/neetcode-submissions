class MyQueue 
{
private:
     stack<int> s1, s2;

    void shiftStacks() 
    {
        //One stack will always be for reading, and one for pushing values, swap when full
        if (s2.empty()) 
        {
            //This shift will only happen if our second stack for reading is empty (ensures proper queue ordering)
            while (!s1.empty()) 
            {
                s2.push(s1.top());
                s1.pop();
            }
        }
    }

public:
    MyQueue() 
    {

    }
    //Push to stack
    void push(int x) 
    {
        s1.push(x);
    }
    
    //Shift to reverse stack and pop
    int pop() 
    {
        shiftStacks();
        int front_element = s2.top();
        s2.pop();
        return front_element;
    }
    //Check top value of our reverse stack
    int peek() 
    {
        shiftStacks();
        return s2.top();
    }
    //Check emptyness of both
    bool empty() 
    {
        return s1.empty() && s2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */