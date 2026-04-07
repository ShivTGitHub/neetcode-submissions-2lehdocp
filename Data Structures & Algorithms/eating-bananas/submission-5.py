class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,hi = 1, max(piles)
        res=hi
        while(l<=hi):
            m=(l+hi)//2
            t=0
            for p in piles:
                t+=(p+m-1)//m
            print(t, m)
            if(t<=h):
                hi=m-1
                res=min(m, res)
            else:
                l=m+1
        return res
            

