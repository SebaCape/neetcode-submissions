# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def goodNodeSearch(root, maxVal):
            if not root:
                return 0
            if root.val >= maxVal:
                return 1 + goodNodeSearch(root.left, root.val) + goodNodeSearch(root.right, root.val)
            return goodNodeSearch(root.left, maxVal) + goodNodeSearch(root.right, maxVal)

        return goodNodeSearch(root, float('-inf'))
        