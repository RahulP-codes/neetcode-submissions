class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size());
        stack<pair<int, int>> st;

        for (int i=0; i<temperatures.size(); i++) {
            int t = temperatures[i];

            while (!st.empty() && t>st.top().first) {
                auto p = st.top();
                res[p.second] = i - p.second;
                st.pop();
            }

            st.push({t, i});
        }

        return res;
    }
};
