class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string res;

        int i =0;
        int l1 = word1.size();
        int l2 = word2.size();

        res.reserve(l1+l2);

        while(i<min(l1,l2)) {
            res.push_back(word1[i]);
            res.push_back(word2[i++]);
        }

        if (l1<l2) {
            res.append(word2, i, l2-i);
        } else {
            res.append(word1, i, l1-i);
        }

        return res;
    }
};