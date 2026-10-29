# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.isValid(root, float("infinity"), float("-infinity"))
    
    def isValid(self, root:Optional[TreeNode], up: int, low: int) -> bool:
        if not root:
            return True
        
        if root.val >= up or root.val <= low:
            return False

        left = self.isValid(root.left, root.val, low)
        right = self.isValid(root.right, up, root.val)

        return left and right
        