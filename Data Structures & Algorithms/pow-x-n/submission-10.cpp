class Solution {
public:
    double myPow(double x, int n) {
        // Use long long to prevent integer overflow when converting INT_MIN to positive
        long long N = n; 
        
        // Handle negative exponents: x^(-n) = (1/x)^n
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        
        double ans = 1.0;
        while (N > 0) {
            // If the current power is odd, multiply the answer by x
            if (N % 2 == 1) {
                ans *= x;
            }
            // Square the base and divide the power by 2
            x *= x;
            N /= 2;
        }
        
        return ans;
    }
};
