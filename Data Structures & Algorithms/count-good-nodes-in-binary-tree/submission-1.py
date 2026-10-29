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

        cnt = 0
        queue = [(root, root.val)]
        while queue:
            node, ma = queue.pop(0)
            if node:
                if node.val >= ma:
                    cnt += 1
                ma = max(node.val, ma)
                queue.append((node.left, ma))
                queue.append((node.right, ma))
            
        return cnt