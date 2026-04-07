class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[[nums[0]]]
        for n in nums[1:]:
            res2=[]
            for r in res:
                # res2.append([])
                for ind in range(len(r)+1):
                    res2.append(r[:ind] + [n] + r[ind:])
            res=res2[:]
        return res