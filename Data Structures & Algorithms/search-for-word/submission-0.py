class Solution:
    def exist(self, bd: List[List[str]], word: str) -> bool:
        def back(ind, r, c):
            if(ind == len(word)):
                return True
            if(
                r == len(bd) or c == len(bd[0]) or
                r < 0 or c < 0 or
                word[ind] != bd[r][c]                
            ):
                return False
            ch = bd[r][c]
            bd[r][c]="#"
            res=(back(ind +1, r, c+1) or
            back(ind +1, r, c-1) or
            back(ind +1, r+1, c) or
            back(ind +1, r-1, c))
            bd[r][c]=ch
            return res
        
        for r in range(len(bd)):
            for c in range(len(bd[0])):
                if back(0, r, c):
                    return True
        return False