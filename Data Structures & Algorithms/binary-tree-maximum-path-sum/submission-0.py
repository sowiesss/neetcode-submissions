# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ma = - math.inf

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            s = left + right + root.val
            self.ma = max(self.ma, s)
            return max(0, root.val + max(left, right))

        dfs(root)
        return self.ma

            
