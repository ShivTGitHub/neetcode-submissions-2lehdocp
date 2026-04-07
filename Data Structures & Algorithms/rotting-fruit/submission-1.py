class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # vis= set()
        nr, nc = len(grid), len(grid[0])
        q = collections.deque()
        fi= 0
        cr=0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    fi+=1
                if(grid[r][c] == 2):
                    q.append((r, c))
        def sprot(r, c):
            # global cr
            nonlocal cr
            # print("sprot", r, c)
            if(not (r in range(nr) and c in range(nc) and grid[r][c]==2)):
                return
            dix= [(-1, 0), (0,-1), (1,0), (0,1)]
            for dr, dc in dix:
                if(not (r+dr in range(nr) and c+dc in range(nc) and grid[r+dr][c+dc]==1)):
                    continue
                q.append((r+dr, c+dc))
                grid[r+dr][c+dc]= 2
                cr+=1
                
            
        res=0
        while(q):
            # print(q)
            l= len(q)
            res+=1
            for i in range(l):
                pr, pc = q.popleft()
                sprot(pr, pc)
        print(cr, fi)
        if(cr != fi):
            return -1
        if(cr==fi==0):
            return 0
        return res-1
