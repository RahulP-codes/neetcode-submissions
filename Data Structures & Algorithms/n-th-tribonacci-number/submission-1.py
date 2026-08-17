class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
            
        ti, ti1, ti2 = 0, 1, 1

        for i in range(2, n):
            ti, ti1, ti2 = ti1, ti2, ti+ti1+ti2

        return ti2