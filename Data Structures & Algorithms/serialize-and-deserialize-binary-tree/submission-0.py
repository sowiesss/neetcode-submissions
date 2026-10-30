# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        l = ""
        q = [root]
        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                if node:
                    l += str(node.val) + "$"
                    q.append(node.left)
                    q.append(node.right)
                else:
                    l += "#$"

        return l
                
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def build(s: str):
            if s == "#":
                return None
            return TreeNode(int(s))

        l = data.split("$")
        if l[0] == '#':
            return None
        
        root = TreeNode(int(l[0]))
        i, n = 0, len(l)
        stk = [root]
        while stk and i < n - 2:
            node = stk.pop(0)
            node.left = build(l[i + 1])
            node.right = build(l[i + 2])
            i += 2
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
            
        return root




