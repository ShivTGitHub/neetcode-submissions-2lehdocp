class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l, r = 0, len(nums)-1
        while(l<=r):
            m=(l+r)//2
            # print(nums[m])
            if(nums[m]==t):
                return m
            if(nums[l]<=nums[m]): #Left half sorted
                if(t>nums[m] or t<nums[l]):
                    l=m+1
                else:
                    r=m-1

            else:                #Right half is sorted
                if(t>nums[r] or t<nums[m]):
                    r=m-1
                else:
                    l=m=1
        return -1