# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        stk = []
        cnt = 0
        curr = root
        
        
        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.left
            node = stk.pop()
            if node:
                cnt += 1
                if cnt == k:
                    return node.val
                curr = node.right
        
        return -1
            
