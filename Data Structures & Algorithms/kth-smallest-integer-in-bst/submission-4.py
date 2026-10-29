# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        cnt = 0
        while curr:
            if not curr.left:
                cnt += 1
                if cnt == k:
                    return curr.val
                curr = curr.right # if leave, right will be the parent
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right

                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    cnt += 1
                    if cnt == k:
                        return curr.val
                    curr = curr.right
        return -1


