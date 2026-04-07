class Solution:
    res=[]
    def combinationSum(self, nums: List[int], t: int) -> List[List[int]]:
        res=[]
        l=t//min(nums)
        def back(ar, cs, ind):
            # print(res)
            if(cs==t):
                res.append(ar[:])
                # ar=[]
                print(ar, res)
                return
            if(cs>t or len(ar)==l):
                return
            # for i in nums:
            #     ar.append(i)
            #     back(ar, cs+i)
            #     ar.pop()
            for i in range(ind, len(nums)):
                ar.append(nums[i])
                back(ar, cs+nums[i], i)
                ar.pop()
        back([], 0, 0)
        return res

