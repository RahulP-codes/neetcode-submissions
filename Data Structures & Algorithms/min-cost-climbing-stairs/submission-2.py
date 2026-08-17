class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        far1, far2 = cost[n-2], cost[n-1]

        for i in range(n-3, -1, -1):
            temp = min(far1, far2)
            far1, far2 = temp + cost[i], far1

        return min(far1, far2)