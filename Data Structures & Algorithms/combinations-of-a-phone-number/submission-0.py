class Solution:
    def letterCombinations(self, ds: str) -> List[str]:
        # kp= {
        #     2 : "ABC",
        #     3 : "DEF",
        #     4 : "GHI",
        #     5 : "JKL",
        #     6 : "MNO",
        #     7 : "PQRS",
        #     8 : "TUV",
        #     9 : "WXYZ",
        # }
        if(len(ds))==0:
            return []
        kp= {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }
        res=[""]
        def back(ind, los):
            if(ind == len(ds)):
                return los
            los2=[]
            for s in los:
                for d in kp[int(ds[ind])]:
                    print(s+d)
                    los2.append(s+d)
            return back(ind + 1, los2)
        return back(0, [""])

        # res = []
        # for i in range(len(digits)):
        #     for j in range(i+1, len(digits)):
        #         for c1 in kp[i]:
        #             for c2 in kp[j]:
        # res=[]
        # lol=[]
        # for i in digits:
        #     lol.append(kp[i])
        # for i in range(len(lol)):
        #     for

