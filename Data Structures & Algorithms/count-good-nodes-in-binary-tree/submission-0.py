# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countGood(root, root.val)
    
    def countGood(self, root: TreeNode, ma: int) -> int:
        if not root:
            return 0
        
        cnt = 0
        if root.val >= ma:
            cnt += 1

        ma = max(root.val, ma)

        left = self.countGood(root.left, ma)
        right = self.countGood(root.right, ma)

        return cnt + left + right
        