# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stk = [(p, q)]

        while stk:
            t1, t2 = stk.pop()
            if (not t1 and t2) or (t1 and not t2):
                return False
            if t1 and t2:
                if t1.val != t2.val:
                    return False
                stk.append((t1.left, t2.left))
                stk.append((t1.right, t2.right))
        return True
                
        
        
        