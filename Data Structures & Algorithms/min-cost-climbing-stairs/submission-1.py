class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        s1, s2 = cost[-1], cost[-2]
        # res= min(s1, s2)
        res1= s1
        if(len(cost)<=3): 
            return min(s1, s2)
        for s in range(len(cost)-3, -1, -1):
            # print(cost[s], s, res)
            res= cost[s] + min(s1, s2)
            s1=s2
            s2=res
            if s==1:
                res1= s2
        return min(res1, s2)


        