# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = [(root, float("inf"), float('-inf'))]
        while queue:
            node, upper, lower = queue.pop(0)
            if node:
                if node.val >= upper or node.val <= lower:
                    return False
                queue.append((node.left, node.val, lower))
                queue.append((node.right, upper, node.val))

        return True