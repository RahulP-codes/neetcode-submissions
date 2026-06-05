class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        int n = asteroids.size();
        stack<int> st;

        for (int ast:asteroids) {
            while(!st.empty() && st.top()+ast<0 && st.top()>0) {
                st.pop();
            }
            if (!st.empty() && st.top()+ast==0 && ast<0) {
                st.pop();
                continue;
            }
            if (!st.empty() && st.top()+ast>0 && ast<0) {
                continue;
            }
            cout<<'y'<<endl;
            st.push(ast);
        }

        vector<int> res(st.size());

        for(int i=st.size()-1; i>=0; i--) {
            res[i] = st.top();
            st.pop();
        }

        return res;
    }
};