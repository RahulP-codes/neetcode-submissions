class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        ref = 0
        ans = []

        minn = min(m, n)

        while ref < (minn+1)//2:
            #top
            for i in range(ref, n-ref):
                ans.append(matrix[ref][i])

            #right
            for i in range(ref+1, m-ref):
                ans.append(matrix[i][n-ref-1])

            #bottom
            if ref < minn//2:
                for i in range(n-ref-2, ref-1, -1):
                    ans.append(matrix[m-ref-1][i])

                #left
                for i in range(m-ref-2, ref, -1):
                    ans.append(matrix[i][ref])

            ref += 1

        return ans
        