class Solution:
    def combinationSum2(self, nums2: List[int], t: int) -> List[List[int]]:
        res=[]
        # s=set(nums)
        # nums2=[i for i in s]
        ss=set()
        
        # cp=1
        def back(ar, ind, cs, cp):
            if(cs == t):
                if(cp not in ss):
                    res.append(ar[:])
                    ss.add(cp)
                return
            
            if(cs > t or ind>=len(nums2)):
                return
            
            ar.append(nums2[ind])
            back(ar, ind+1, cs+nums2[ind], cp*nums2[ind])
            ar.pop()
            ind+=1
            while(ind < len(nums2) and nums2[ind-1] == nums2[ind]):
                ind+=1
            back(ar, ind, cs, cp)
        back([], 0, 0, 1)
        return res