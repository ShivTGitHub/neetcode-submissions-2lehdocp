class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res= 0
        nr , nc = len(grid), len(grid[0])
        vis= set()
        def dfs(r, c):
            if(not (r in range(nr) and c in range(nc) and (r, c) not in vis and grid[r][c]=="1")):
                return 
            s= []

            s.append((r, c))
            vis.add((r, c))
            while(s):
                pr, pc= s.pop()
                dirc= [(-1, 0), (0, 1),(1, 0), (0, -1) ]
                for dr, dc in dirc:
                    if((pr+dr) in range(nr) and (pc+dc) in range(nc) and
                        grid[pr+dr][pc+dc]=="1" and (dr+pr, dc+pc) not in vis):
                            s.append((pr+dr, pc+dc))
                            vis.add((pr+dr, pc+dc))
        for r in range(nr):
            for c in range(nc):
                if((r, c) not in vis and grid[r][c]=="1"):
                    dfs(r,c)
                    res+=1
        return res
