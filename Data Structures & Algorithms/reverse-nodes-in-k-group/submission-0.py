# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrevious = dummy #holds the node before the start of our current group

        while True:
            kth = self.getKth(groupPrevious, k)

            if not kth:
                break

            groupNext = kth.next

            #reverse group
            prev, curr = kth.next, groupPrevious.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrevious.next
            groupPrevious.next = kth
            groupPrevious = temp

        return dummy.next
    
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr