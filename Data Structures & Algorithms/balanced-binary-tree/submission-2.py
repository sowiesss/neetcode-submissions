# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stk = [root]
        curr = root
        height = {None: 0}
        while stk:
            curr = stk[-1]
            if curr.left and curr.left not in height:
                stk.append(curr.left)
                
            elif curr.right and curr.right not in height:
                stk.append(curr.right)
                
            else:
                stk.pop()
                left = height[curr.left]
                right = height[curr.right]
                if abs(left - right) > 1:
                    return False
                height[curr] = 1 + max(left, right)
        
        return True


        