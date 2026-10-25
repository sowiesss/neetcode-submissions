# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height = self.maxHeight(root)
        if height == -1:
            return False
        return True      

    
    def maxHeight(self, root: Optional[TreeNode]):
        if not root:
            return 0

        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return 1 + max(left, right)