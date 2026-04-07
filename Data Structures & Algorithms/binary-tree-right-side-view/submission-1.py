# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ll=[[root]]
        res=[root.val]
        while(ll):
            pl=ll.pop()
            apl=[]
            il=len(res)
            for p in pl[::-1]:
                # print("Here")
                # print(ll, pl, apl)
                if(p.right):
                    apl.append(p.right)
                    if(il==len(res)):
                        res.append(p.right.val)
                
                if(p.left):
                    apl.append(p.left)
                    if(il==len(res)):
                        res.append(p.left.val)
            if(len(apl)>0):
                ll.append(apl[::-1])
        return res