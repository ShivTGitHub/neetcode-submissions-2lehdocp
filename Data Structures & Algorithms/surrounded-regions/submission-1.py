class Solution:
    def solve(self, bd: List[List[str]]) -> None:
        nr ,nc = len(bd), len(bd[0])

        def trav(r, c):
            if(r not in range(nr) or c not in range(nc) or bd[r][c] != "O"):
                return 
            bd[r][c] = "*"
            trav(r+1, c)
            trav(r, c+1)
            trav(r-1, c)
            trav(r, c-1)

        for c in range(nc):
            trav(0,c)
        for c in range(nc):
            trav(nr-1,c)
        for r in range(nr):
            trav(r, 0)
        for r in range(nr):
            trav(r, nc-1)
        for r in range(nr):
            for c in range(nc):
                if(bd[r][c] == "*"):
                    bd[r][c] = "O"
                else:
                    bd[r][c] = "X"
        return
