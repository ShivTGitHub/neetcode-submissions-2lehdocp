# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res=True
        def dfs(node):
            # lf=[]
            if not node:
                # lf.append("Null")
                # print(lf)
                return 0
            
            # lf.append("Not Null")
            # lf.append(node.val)
            l=dfs(node.left)
            r=dfs(node.right)
            # lf.append(l)
            # lf.append(r)
            if(not (-1<=l-r and l-r<=1)):
                # lf.append("not balanced")
                self.res=False
            # lf.append("balanced")
            # lf.append(1+l+r)
            # print(lf)
            
            return 1+max(l,r)
        dfs(root)
        return self.res
