class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for b in s:
            if(b == "}"):
                if(len(st)>0 and st[-1] == "{"):
                    st.pop()
                else:
                    return False
            
            elif(b == "]"):
                if(len(st)>0 and st[-1] == "["):
                    st.pop()
                else:
                    return False
            elif(b == ")"):
                if(len(st)>0 and st[-1] == "("):
                    st.pop()
                else:
                    return False
            else:
                st.append(b)
            
        if len(st)>0:
            return False
        return True
