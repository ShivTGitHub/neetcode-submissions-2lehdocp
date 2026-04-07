class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sl=nums[0]
        fa=nums[nums[0]]
        while(fa!=sl):
            sl=nums[sl]
            fa=nums[nums[fa]]
        
        # sl2=0
        sl2=0
        while(sl2!=sl):
            sl=nums[sl]
            sl2=nums[sl2]
        return sl2

        
