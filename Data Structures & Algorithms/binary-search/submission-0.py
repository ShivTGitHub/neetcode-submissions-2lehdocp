class Solution:
    def search(self, nums: List[int], tr: int) -> int:
        hi=len(nums)-1
        lo=0
        while(hi>lo):
            m=(hi+lo)//2
            if tr>nums[m]:
                lo=m+1
            elif tr<nums[m]:
                hi=m-1
            else:
                return m
        if nums[(hi+lo)//2]==tr:
            return (hi+lo)//2
        return -1