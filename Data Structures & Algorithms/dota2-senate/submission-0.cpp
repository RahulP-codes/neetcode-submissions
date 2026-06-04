class Solution {
public:
    string predictPartyVictory(string senate) {
        int rcnt = 0, i = 0;

        while (i<senate.size()) {
            if (senate[i]=='R') {
                if (rcnt < 0) {
                    senate.push_back('D');
                }
                rcnt++;
            } else {
                if (rcnt > 0) {
                    senate.push_back('R');
                }
                rcnt--;
            }
            i++;
        }

        return (rcnt>0) ? "Radiant":"Dire";
    }
};