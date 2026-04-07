class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        s=[]
        def back(op, cl):
            if(op==cl==n):
                res.append("".join(s))
                return 
            if(op<n):
                s.append("(")
                back(op+1, cl)
                s.pop()
            # s.pop()
            if(op>cl):
                s.append(")")
                back(op, cl+1)
                s.pop()
        back(0,0)
        return res
