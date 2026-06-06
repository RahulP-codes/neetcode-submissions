class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        stack<int> pmin, nmin;

        vector<int> baseLen(n);

        for (int i=n-1; i>=0; i--) {
            while(!nmin.empty() && heights[nmin.top()]>=heights[i]) {
                nmin.pop();
            }
            baseLen[i]=(nmin.empty()) ? n:nmin.top();
            nmin.push(i);
        }

        for (int i=0; i<n; i++) {
            while(!pmin.empty() && heights[pmin.top()]>heights[i]) {
                pmin.pop();
            }
            int fix=(pmin.empty()) ? -1:pmin.top();
            baseLen[i] -= fix+1;
            pmin.push(i);
        }

        int maxx = 0;
        for (int i=0; i<n; i++) {
            int area = heights[i]*baseLen[i];
            maxx = max(maxx, area);
        }

        return maxx;
    }
};