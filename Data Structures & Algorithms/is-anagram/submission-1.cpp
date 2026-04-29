class Solution {
public:
    bool isAnagram(string s, string t) {
        int slen = s.length();
        if (slen != t.length()) return false;

        vector<int> count(26);

        for (int i=0; i<slen; i++) {
            count[s[i]-'a']++;
            count[t[i]-'a']--;
        }

        for (int i: count) {
            if (i != 0) return false;
        }

        return true;
    }
};