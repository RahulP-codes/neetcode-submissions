class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        far1, far2 = 2, 1
        for i in range(n-2):
            far1, far2 = far1+far2, far1

        return far1