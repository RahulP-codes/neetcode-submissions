class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
            
        n = len(s)

        farthest = 0
        canJump = [False]*len(s)
        canJump[0] = True

        for i in range(n):
            print("i:", i)
            print(farthest)
            if canJump[i]:
                for j in range(max(farthest, i+minJump), min(i+maxJump+1, n)):
                    if j == n-1:
                        return True
                    if s[j] == '0':
                        canJump[j] = True
                    farthest = j+1
        
        return False
