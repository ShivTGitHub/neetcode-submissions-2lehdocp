class Solution {
public:
    bool isAnagram(string s, string t) {
        int s1=1;
        int s2=1;
        for(char c: s){s1*=c-'a'+1;}
        for(char c: t){s2*=c-'a'+1;}
        cout<<s1<<endl;
        cout<<s2<<endl;
        if(s1!=s2){return false;}
        return true;
    }
};
