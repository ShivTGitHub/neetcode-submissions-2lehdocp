class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& trt) {
        stack<pair<int, int>> st; // temp, ind
        vector<int> res(trt.size(), 0);
        for(int i=0; i<trt.size(); i++){
            while(!st.empty() && trt[i]>st.top().first){
                res[st.top().second]=(i-st.top().second);
                st.pop();
            }
            st.push({trt[i], i});
        }
        return res;

    }
};
