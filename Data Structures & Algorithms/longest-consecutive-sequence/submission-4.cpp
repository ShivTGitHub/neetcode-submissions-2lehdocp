class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0){return 0;}
        if(nums.size()==1){return 1;}
        unordered_set<int> st;
        int res=1;
        int len=0;
        for(int i : nums){st.insert(i);}
        for(int i : st){
            if(st.find(i-1)!=st.end()){
                int n=i;
                len=1;
                while(st.find(i-1)!=st.end()){len++; i--;}
                while(st.find(n+1)!=st.end()){len++; n++;}
                res=max(res, len);
            }
        }
        // res=max(res, len);
        return res;
        
    }
};
