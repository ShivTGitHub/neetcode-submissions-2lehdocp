class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if(len(heights)==2 and 0 in heights):
            return 0
        l=0
        r=len(heights)-1
        vol=1
        while(l<r):
            # global vol1
            vol=max(vol, (r-l)*min(heights[l], heights[r]))
            if(heights[l]<heights[r]):
                l+=1
            else:
                r-=1
        return vol