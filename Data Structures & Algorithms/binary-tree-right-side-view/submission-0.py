# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        level = [root]
        while level:
            lenth = len(level)
            right = level[-1]
            res.append(right.val)
            nextl = []
            while level:
                n = level.pop(0)
                if n.left:
                    nextl.append(n.left)
                if n.right:
                    nextl.append(n.right)
            level = nextl
            
        return res


    