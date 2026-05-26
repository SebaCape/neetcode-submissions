# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            right = None
            qlen = len(q)

            for i in range(qlen):
                cur = q.popleft()
                if cur:
                    right = cur
                    q.append(cur.left)
                    q.append(cur.right)

            if right:
                res.append(right.val)

        return res