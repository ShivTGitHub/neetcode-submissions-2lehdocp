"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if(not node):
            return None
        old2new = {} #val -> node obj
        def trav(nd):
            copy = Node(nd.val, [])
            old2new[copy.val] = copy
            for nb in nd.neighbors:
                if(nb.val in old2new):
                    copy.neighbors.append(old2new[nb.val])
                else:
                    copy.neighbors.append(trav(nb))
            return copy
        return trav(node)