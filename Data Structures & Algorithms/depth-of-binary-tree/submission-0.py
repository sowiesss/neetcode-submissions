# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.count(root, 0)

    def count(self, root: Optional[TreeNode], depth: int) -> int:
        if not root: return 0

        dl = self.count(root.left, depth)
        dr = self.count(root.right, depth)

        return max(dl, dr) + 1