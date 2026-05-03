class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        vector<int> ans(26);

        for (int i = 0; i<s.size(); i++) {
            ans[s[i]-'a']++;
            ans[t[i]-'a']--;
        }

        for (int a:ans) {
            if (a) {
                return false;
            }
        }

        return true;
    }
};