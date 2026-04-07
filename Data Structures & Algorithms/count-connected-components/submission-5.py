class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vis= set()
        res=0
        mp= {i: [] for i in range(n)}
        def dfs(node):
            if(node in vis):
                return
            vis.add(node)
            for v in mp[node]:
                dfs(v)
        

        for v1, v2 in edges:
            mp[v1].append(v2)
            mp[v2].append(v1)
        for v in range(n):
            if(v in vis):
                continue
            dfs(v)
            vis.add(v)
            res+=1
        return res
            
        