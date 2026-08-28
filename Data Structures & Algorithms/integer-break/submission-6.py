class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2

        n_3 = 1
        n_2 = 2
        n_1 = 3

        for num in range(4, n+1):
            n_1, n_2, n_3 = max(2*n_2, 3*n_3), n_1, n_2

        return n_1