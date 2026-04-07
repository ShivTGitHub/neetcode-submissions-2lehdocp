class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        unordered_map<int,vector<int>> pm;
        vector<int> res;
        for(int i : nums){
            if(mp.find(i)!=mp.end()){mp[i]++;}
            else{mp[i]=1;}
        }
        int cnt=0;
        for(auto it : mp){
            cout<<it.second<<" --- "<<it.first<<endl;
            if(pm.find(it.second)!=pm.end()){pm[it.second].push_back(it.first);}
            else{
                vector<int> v={it.first};
                pm[it.second]=v;
                cnt=max(cnt, it.second);
            }
        }
        while(cnt>0){
            if(pm.find(cnt)!=pm.end()){
                for(int j: pm[cnt]){
                    if(k==0){return res;}
                    else{res.push_back(j); k--;}
                }
            }
            cnt--;
        }

        
        return res;
    }
};
