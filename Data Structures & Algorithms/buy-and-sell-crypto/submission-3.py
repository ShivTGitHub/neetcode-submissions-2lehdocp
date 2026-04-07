class Solution:
    def maxProfit(self, ps: List[int]) -> int:
        b=0
        s=1
        res=0
        while(b<len(ps) and s<len(ps)):
            res=max(res, ps[s]-ps[b])
            if ps[s]<ps[b]:
                b=s
                # s+=1
            s+=1
        return res
