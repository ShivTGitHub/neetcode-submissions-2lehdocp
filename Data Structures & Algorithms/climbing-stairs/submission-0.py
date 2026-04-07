class Solution:
    def climbStairs(self, n: int) -> int:
        res=[0]
        def back(c):
            if(c==n):
                res[0]+=1
                return
            if(c>n):
                return
            back(c+1)
            back(c+2)

        back(0)
        return res[0]