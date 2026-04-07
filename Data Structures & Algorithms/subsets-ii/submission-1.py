class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        nums.sort()
        def back(ind, ar):
            
            if(ind == len(nums)):
                # res.append(ar[:])
                return 
            ar.append(nums[ind])
            res.append(ar[:])
            back(ind+1, ar)
            while(ind < len(nums)-1):
                if nums[ind] == nums[ind+1]:
                    ind+=1
                else:
                    break
            ar.pop()
            back(ind+1, ar)
        back(0, [])
        print(nums)
        return res