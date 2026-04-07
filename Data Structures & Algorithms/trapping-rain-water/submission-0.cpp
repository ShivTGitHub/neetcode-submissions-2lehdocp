class Solution {
public:
    int trap(vector<int>& ht) {
        vector<int> lmax;
        vector<int> rmax;
        int l=ht[0];
        int r=ht[ht.size()-1];

        for(int i=0; i<ht.size(); i++){
            l=max(l, ht[i]);
            lmax.push_back(l);
            r=max(r, ht[ht.size()-1-i]);
            rmax.push_back(r);
        }
        // for(int i: lmax){cout<<i;}
        // cout<<endl;
        reverse(rmax.begin(), rmax.end());
        // for(int i: rmax){cout<<i;}111
        int res=0;
        for(int i=0; i<ht.size(); i++){
            res+=min(lmax[i], rmax[i])-ht[i];
        }

        return res;
    }
};
