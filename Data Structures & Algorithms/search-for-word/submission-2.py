class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h = len(board)
        w = len(board[0])
        
        visited = set([])

        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if i < 0 or i >= h:
                return False
            if j < 0 or j >= w:
                return False
            if (i, j) in visited:
                return False

            res = False
            if board[i][j] == word[idx]:
                visited.add((i, j))

                res = (dfs(i-1, j, idx+1)
                    or dfs(i+1, j, idx+1)
                    or dfs(i, j-1, idx+1)
                    or dfs(i, j+1, idx+1))
                
                visited.remove((i, j))

            if res:
                return res

            if idx == 0:
                if j+1 == w:
                    res = dfs(i+1, 0, 0)
                else:
                    res = dfs(i, j+1, 0)

            return res

        return dfs(0, 0, 0)