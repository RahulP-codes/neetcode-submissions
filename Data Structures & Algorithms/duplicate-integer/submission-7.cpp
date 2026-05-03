class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        vector<int> ref;
        for (int num: nums) {
            if (find(ref.begin(), ref.end(), num)!=ref.end()) {
                return true;
            }
            ref.push_back(num);
        }
        return false;
    }
};