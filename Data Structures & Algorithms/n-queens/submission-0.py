class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        stack = []

        # Tracking sets or arrays for columns and both diagonals
        cols = [False] * n
        diag1 = [False] * (2 * n - 1)  # i + j
        diag2 = [False] * (2 * n - 1)  # i - j + n - 1

        def pos_str(j):
            return "." * j + "Q" + "." * (n - j - 1)

        def df(i):
            # Base Case: All rows filled successfully
            if i == n:
                res.append(stack[:])
                return

            # Try placing a queen in each column 'j' of the current row 'i'
            for j in range(n):
                # Calculate the unique diagonal identifiers
                d1 = i + j
                d2 = i - j + (n - 1)

                # Check if safe
                if not (cols[j] or diag1[d1] or diag2[d2]):
                    # 1. Action: Place the queen and mark the paths as blocked
                    cols[j] = diag1[d1] = diag2[d2] = True
                    stack.append(pos_str(j))

                    # 2. Recurse to the next row
                    df(i + 1)

                    # 3. Backtrack: Clean up our mess for the next iteration!
                    stack.pop()
                    cols[j] = diag1[d1] = diag2[d2] = False

        df(0)
        return res
