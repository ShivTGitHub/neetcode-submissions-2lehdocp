class Solution:
    def validTree(self, n: int, ed: List[List[int]]) -> bool:
        mp = {i : [] for i in range(n)}
        for n1, n2 in ed:
            mp[n1].append(n2)
            mp[n2].append(n1)
        v = set()

        def dfs(nd, pr):
            if(nd in v):
                return False
            v.add(nd)
            for i in mp[nd]:
                if (i == pr):
                    continue
                if(not dfs(i, nd)):
                    return False
            return True
        return dfs(0, -1) and len(v) == n

