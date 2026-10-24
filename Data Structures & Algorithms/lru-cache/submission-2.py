class LRUCache:

    def __init__(self, capacity: int):
        self.l_h = Node(0, 0)
        self.r_h = Node(0, 0)
        self.l_h.nex = self.r_h
        self.r_h.prev = self.l_h
        self.capacity = capacity
        self.key_to_node = {}
        

    def get(self, key: int) -> int:
        n = self.key_to_node.get(key)
        if not n:
            return -1

        Node.remove(n)
        Node.addRight(n, self.r_h)

        return n.val


    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            Node.remove(node)
            Node.addRight(node, self.r_h)

        else:
            if self.capacity <= len(self.key_to_node):
                pop = self.l_h.nex
                Node.remove(pop)
                self.key_to_node.pop(pop.key)
                
            node = Node(value, key)
            Node.addRight(node, self.r_h)
            self.key_to_node[key] = node

        

class Node:

    def __init__(self, val: int, key: int, prev: Node = None, nex: Node = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.nex = nex


    @staticmethod
    def remove(node: Node):
        prev = node.prev
        nex = node.nex
        prev.nex = nex
        nex.prev = prev


    @staticmethod
    def addRight(node: Node, right_head: Node):
        r_prev = right_head.prev
        r_prev.nex = node
        node.prev = r_prev
        node.nex = right_head
        right_head.prev = node
    
