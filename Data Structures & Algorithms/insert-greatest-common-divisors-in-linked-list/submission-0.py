# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(n1, n2):
            while n2 != 0:
                n1, n2 = n2, n1 % n2
            return n1

        cur = head

        while cur and cur.next:
            i_val = ListNode(gcd(cur.val, cur.next.val))

            i_val.next = cur.next
            cur.next = i_val
            cur = cur.next.next

        return head