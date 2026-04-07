class Solution:
    def minEatingSpeed(self, pl: List[int], h: int) -> int:
        l=1
        r=max(pl)
        res=r
        while(l<=r):
            m=(l+r)//2
            t=0
            for i in pl:
                t+=i//m
                if(i%m!=0):
                    t+=1
            if(t<=h):
                res=min(res, m)
                r=m-1
            else:
                l=m+1
                
        # res=min(res, m)
        return res
