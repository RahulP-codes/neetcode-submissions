class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> ref;
        for (int num: nums) {
            if (ref.count(num)) {
                return true;
            }
            ref.insert(num);
        }
        return false;
    }
};