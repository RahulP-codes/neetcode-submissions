class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector<int> temp;

        for (int num: nums) {
            if (num != val) {
                temp.push_back(num);
            }
        }
        for (int i=0; i<temp.size(); i++) {
            nums[i] = temp[i];
        }

        return temp.size();
    }
};