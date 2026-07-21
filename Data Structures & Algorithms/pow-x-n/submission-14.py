class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        elif n < 0:
            x = 1/x
            n = -n

        ans = 1
        r = 1

        while n:
            if n%2:
                ans *= x
            
            x *= x
            n = n//2

        return ans