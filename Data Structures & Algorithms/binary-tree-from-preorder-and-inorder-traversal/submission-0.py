# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = preorder[0]
        ind = inorder.index(root)
        leftin = inorder[0:ind]
        rightin = inorder[ind + 1:]
        leftpre = preorder[1: ind + 1]
        rightpre = preorder[ind + 1:]
        
        r = TreeNode(root)
        left = self.buildTree(leftpre, leftin)
        right = self.buildTree(rightpre, rightin)
        r.left = left
        r.right = right
        return r
