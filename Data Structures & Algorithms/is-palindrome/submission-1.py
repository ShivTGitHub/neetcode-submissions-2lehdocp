class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r= 0, len(s)-1
        while(l<r):
            while(not s[r].isalnum() and l<r):
                r-=1
            while(not s[l].isalnum() and l<r):
                l+=1
            # print(s[l], s[r])
            if(s[l].lower() != s[r].lower()):
                # print(l, s[l], r, s[r])
                return False
            r-=1
            l+=1
        return True