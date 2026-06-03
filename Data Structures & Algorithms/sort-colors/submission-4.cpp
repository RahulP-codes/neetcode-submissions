class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> count(2, 0);

        for (int num:nums) {
            if (num == 2) continue;
            count[num]++;
        }

        for (int i = 0; i<nums.size(); i++) {
            if (i < count[0]) {
                nums[i] = 0;
            } else if (i < count[1]+count[0]) {
                nums[i] = 1;
            } else {
                nums[i] = 2;
            }
        }
    }
};