class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        st = set(nums)
        # l=1
        res=1
        for s in st:
            ts=s
            l=1
            while(ts-1 in st):
                ts-=1
                l+=1
            res=max(res, l)
        return res

