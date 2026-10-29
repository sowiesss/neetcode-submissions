# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.kth(root, k, 0)[0]

    def kth(self, root, k, ind) -> tuple:
        if not root:
            return (-1, ind)
        # print(root.val, ind)
        
        left, lind = self.kth(root.left, k, ind)

        if lind < k - 1:
            lind += 1
            right, rind = self.kth(root.right, k, lind)
            if right < 0:
                return (root.val, lind)

            return (right, rind)

        elif lind == k - 1:
            return (root.val, k)
        else:
            return (left, lind)
            
        
        
        

        