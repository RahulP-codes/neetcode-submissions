class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int l = 0, r = matrix[0].size()-1;
        int u = 0, d = matrix.size()-1;

        vector<int> res;

        while(l<=r && u<=d) {
            //top
            for (int i = l; i < r+1; i++) {
                res.push_back(matrix[u][i]);
            }
            u++;
            //right
            for (int i = u; i < d+1; i++) {
                res.push_back(matrix[i][r]);
            }
            r--;

            if (!(l<=r && u<=d)) {
                break;
            }
            //down
            for (int i = r; i >= l; i--) {
                res.push_back(matrix[d][i]);
            }
            d--;
            //right
            for (int i = d; i >= u; i--) {
                res.push_back(matrix[i][l]);
            }
            l++;
        }

        return res;
    }
};
