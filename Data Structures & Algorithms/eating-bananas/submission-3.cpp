class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int maxx = *max_element(piles.begin(), piles.end());

        int l = 1, r = maxx;
        int ans;
        while (l<=r) {
            int k = (l+r)/2;

            int totalTime = 0;
            for (int p:piles) {
                totalTime += (p+k-1)/k;
            }

            if (totalTime <= h) {
                ans = k;
                r = k - 1;
            } else l = k + 1;
        }

        return ans;
    }
};
