class Solution:
    def climbStairs(self, n: int) -> int:
        def back(s):
            if(s>=n):
                return s == n
            return back(s+1) + back(s+2)
        return back(0)