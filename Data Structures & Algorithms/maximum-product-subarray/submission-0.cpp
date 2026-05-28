class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();

        int prod = 1;
        int prod2 = 1;
        int maxProd = nums[0];

        int negCount = 0;

        for (int i=0; i<n; i++) {
            prod *= nums[i];
            maxProd = max(prod, maxProd);

            if (negCount > 0) {
                prod2 *= nums[i];
                maxProd = max(maxProd, prod2);
            }
            if (nums[i] < 0) negCount++;

            if (nums[i] == 0) {
                negCount = 0;
                prod = 1;
                prod2 = 1;
            }

        }

        return maxProd;
    }
};