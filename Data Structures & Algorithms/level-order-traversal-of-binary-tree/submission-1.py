# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        self.dfs(root, 0, res)
        
        return res
                

    def dfs(self, root, depth, res):
        if not root:
            return
        
        if len(res) < depth + 1:
            l = [root.val]
            res.append(l)
        else:
            res[depth].append(root.val)

        self.dfs(root.left, depth + 1, res)
        self.dfs(root.right, depth + 1, res)
        