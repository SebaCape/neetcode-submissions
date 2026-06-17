/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) 
    {
        //Edge case (no list is acyclic by vacuous truth)
        if(!head)
            return false;

        //Fast & slow pointer to check for cycling
        ListNode *fast = head, *slow = head;

        while(fast->next && fast->next->next)
        {
            fast = fast->next->next;
            slow = slow->next;
            //Equality == cycle
            if(slow == fast)
                return true;
        }
            
        //Otherwise none exists
        return false;
    }
};