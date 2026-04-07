class Solution:
    def isValidSudoku(self, bd: List[List[str]]) -> bool:
        rows=[set(i for i in range(1,10)) for i in range(9)]
        # rows=[[i for i in range(1,10)]*9]
        cols=[set(i for i in range(1,10)) for i in range(9)]
        # grd=rows
        grd=[[set(i for i in range(1,10)) for i in range(3)] for i in range(3)]
        # print(grd)
        for r in range(9):
            for c in range(9):
                if bd[r][c]==".":
                    continue
                gr=r//3
                gc=c//3
                el=int(bd[r][c])
                # print(el, r, c, end=".......")
                if el in rows[r] and el in cols[c] and el in grd[gr][gc]:
                    rows[r].remove(el)
                    cols[c].remove(el)
                    grd[gr][gc].remove(el)
                # if el in rows[r]:
                #     print("in row")
                #     if el in cols[c]:
                #         print("in col")
                #         if el in grd[gr][gc]:
                #             print(gr, gc, "in grd")

                else:
                    return False
        return True

                    
        # print(rows)
        # for i in rows:
        #     print(type(i), i)
        return False