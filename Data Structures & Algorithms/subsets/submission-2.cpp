class Solution {
public:
    vector<vector<int>> res;
    vector<int> l;

    void back(int i, vector<int> num){
        if(i==num.size()){res.push_back(l); return;}
        l.push_back(num[i]);
        back(i+1, num);
        l.pop_back();
        back(i+1, num);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        back(0, nums);
        return res;
    }
};