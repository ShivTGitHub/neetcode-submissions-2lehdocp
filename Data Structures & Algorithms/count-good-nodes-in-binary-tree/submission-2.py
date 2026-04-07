# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res=0
    def goodNodes(self, root: TreeNode) -> int:
        # res=0
        def back(node, m):
            # m=max(m, node.val)
            if not node:
                return 
            if(node.val >= m):
                self.res+=1
                m=node.val
            if(node.left):
                back(node.left, m)
            if(node.right):
                back(node.right, m)

        back(root, root.val)
        return self.res
            
