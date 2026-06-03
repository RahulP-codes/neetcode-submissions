class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int row;
        for (row = 0; row<matrix.size()-1; row++) {
            if (matrix[row][0] <= target && target < matrix[row+1][0]) {
                break;
            }
        }

        for (int num:matrix[row]) {
            if (num == target) return true;
        }

        return false;
    }
};
