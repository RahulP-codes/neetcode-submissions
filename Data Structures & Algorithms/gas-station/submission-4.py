class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        totalSum = 0
        curSum = -1
        ans = -1
        prev = -1

        for i in range(n):
            cur = gas[i] - cost[i]
            totalSum += cur

            if curSum < 0 and cur >= 0:
                ans = i

            if curSum < 0:
                curSum = 0
            curSum += cur

        return ans if totalSum >= 0 else -1