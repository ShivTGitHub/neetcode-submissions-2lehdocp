# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        ll=[[root]]
        res=[[root.val]]
        # ll.append([1,2,3,4])
        
        # while(ll)
        # print(ll.pop())
        while(ll):
            pl=ll.pop()
            if(len(pl)==0):
                res.pop()
                return res
            res.append([])
            ll.append([])
            for p in pl:
                if(p.left):
                    ll[-1].append(p.left)
                    res[-1].append(p.left.val)
                if(p.right):
                    ll[-1].append(p.right)
                    res[-1].append(p.right.val)

        # res.pop()
        return res