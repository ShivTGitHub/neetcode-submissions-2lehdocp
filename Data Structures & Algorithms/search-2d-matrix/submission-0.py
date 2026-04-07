class Solution:
    def searchMatrix(self, mx: List[List[int]], tr: int) -> bool:
        hi=len(mx)-1
        lo=0
        while(hi>=lo):
            m=(hi+lo)//2
            print(mx[m])
            if mx[m][-1]<tr:
                lo=m+1
            elif mx[m][-1]>tr:
                if mx[m][0]>tr:
                    hi=m-1
                else:
                    if tr in mx[m]:
                        return True
                    else:
                        return False
            else:
                return True

        # if tr in mx[m]:
        #     return True        
        return False