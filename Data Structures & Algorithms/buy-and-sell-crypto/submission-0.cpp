class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPr = prices[0];
        int maxProf = 0;

        for (int p:prices) {
            if (minPr>p) {
                minPr = p;
            }
            maxProf = max(maxProf, p-minPr);
        }

        return maxProf;
    }
};
