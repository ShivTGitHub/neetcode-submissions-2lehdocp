class Solution:
    def pacificAtlantic(self, ht: List[List[int]]) -> List[List[int]]:
        nr, nc= len(ht), len(ht[0])
        vis=set()
        def toP(r, c):
            if(r==0):
                return True
            if(c==0):
                return True
            if(not (r in range(nr) and c in range(nc) and (r,c) not in vis)):
                return False
            res= False
            vis.add((r,c))
            dix=[(0,1),(1,0),(-1,0),(0,-1)]
            for dr, dc in dix:
                if(dr+r in range(nr) and c+dc in range(nc) and 
                    ht[r][c] >= ht[r+dr][c+dc]):
                    res= res or toP(r+dr, c+dc)
            return res

        
        def toA(r, c):
            if(r==nr-1):
                return True
            if(c==nc-1):
                return True
            if(not (r in range(nr) and c in range(nc) and (r,c) not in vis)):
                return False
            res= False
            vis.add((r,c))
            dix=[(0,1),(1,0),(-1,0),(0,-1)]
            for dr, dc in dix:
                if(dr+r in range(nr) and c+dc in range(nc) and 
                    ht[r][c] >= ht[r+dr][c+dc]):
                    res= res or toA(r+dr, c+dc)
            return res
        can=[]
        for r in range(nr):
            for c in range(nc):
                vis.clear()
                res1= toP(r,c)
                vis.clear()
                res2= toA(r,c)
                if(res1 and res2):
                    can.append([r,c])
        return can

        


            
