class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        dp = [[] for _ in range(n+1)]
        dp[0].append("")

        for i in range(1, n+1):
            for j in range(i):
                for left in dp[j]:
                    for right in dp[i-j-1]:
                        dp[i].append("(" + left + ")" + right)

        return dp[n]
            

        
        