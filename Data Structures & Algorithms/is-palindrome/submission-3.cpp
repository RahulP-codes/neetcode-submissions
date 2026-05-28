class Solution {
public:
    bool isPalindrome(string s) {
        int lp = 0;
        int rp = s.size()-1;

        char l = ' ';
        char r = ' ';

        while (lp<rp) {
            while(!isalnum(tolower(s[lp]))) lp++;
            while(!isalnum(tolower(s[rp]))) rp--;

            if(lp>rp) {
                break;
            }

            l = tolower(s[lp]);
            lp++;

            r = tolower(s[rp]);
            rp--;

            cout << l << r << endl;
            if (l != r) {
                return false;
            }
        }

        return true;
    }
};
