# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        res = 0

        def kth(root: Optional[TreeNode]):
            nonlocal res, cnt

            if not root or res:
                return
            
            kth(root.left)
            cnt += 1
            if cnt == k:
                res = root.val
            kth(root.right)

        kth(root)
        return res
            
        
        
        

        