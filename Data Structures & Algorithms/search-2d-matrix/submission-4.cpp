class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();

        int top = 0, bot = m-1;
        int row;
        while (top <= bot) {
            row = (top+bot)/2;

            if (target < matrix[row][0]) {
                bot = row - 1;
                continue;
            } else if (target <= matrix[row][n-1]) {
                break;
            } else top = row + 1;
        }

        int left = 0, right = n-1;
        int mid;
        while (left<=right) {
            mid = (left+right)/2;

            if (target < matrix[row][mid]) {
                right = mid -1;
                continue;
            } else if(matrix[row][mid] == target) {
                return true;
            } else left = mid + 1;
        }
        return false;
    }
};
