class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        step2 = cost[0]
        step1 = cost[1]

        for i in range(2, n):
            if step1 <= step2:
                step1, step2 = step1+cost[i], step1
            else:
                step1, step2 = step2+cost[i], step1

        return min(step1, step2)
        