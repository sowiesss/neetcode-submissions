# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        map = {}
        map[None] = (0, 0)
        stk = [root]
        
        while stk:
            node = stk[-1]
            if node.left and node.left not in map:
                stk.append(node.left)
            elif node.right and node.right not in map:
                stk.append(node.right)
            else:
                stk.pop()
                diameter = map[node.left][0] + map[node.right][0]
                maxh = 1 + max(map[node.left][0], map[node.right][0])            
                maxd = max(diameter, map[node.left][1], map[node.right][1])
                map[node] = (maxh, maxd)

        return map[root][1]
