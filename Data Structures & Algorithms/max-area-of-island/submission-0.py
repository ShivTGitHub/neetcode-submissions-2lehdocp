class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nr, nc= len(grid), len(grid[0])
        def dfs(r, c):
            if(not (r in range(nr) and c in range(nc) and
            grid[r][c]==1)):
                # print(909090)
                return 0

            s = collections.deque()
            s.append((r,c))
            grid[r][c]= -1
            res=0
            # print(999999)
            while(s):
                dix = [(-1, 0), (0, -1), (1, 0), (0,1)]
                pr, pc = s.popleft()
                for dr, dc in dix:
                    res+=dfs(pr+dr, pc+dc)
                print(res)
            return 1+res
        maxi=0
        for r in range(nr):
            for c in range(nc):
                n = dfs(r,c)
                maxi=max(maxi, n)
        return maxi




