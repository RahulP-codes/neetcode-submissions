class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int prod = 1;
        int prod2 = 1;
        int maxProd = nums[0];

        int negCount = 0;

        for (int num:nums) {
            prod *= num;
            maxProd = max(prod, maxProd);

            if (negCount > 0) {
                prod2 *= num;
                maxProd = max(maxProd, prod2);
            }
            if (num < 0) negCount++;

            if (num == 0) {
                negCount = 0;
                prod = 1;
                prod2 = 1;
            }

        }

        return maxProd;
    }
};