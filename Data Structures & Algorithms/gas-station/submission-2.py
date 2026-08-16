class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        totalSum = 0
        curSum = 0
        ans = -1
        prev = -1

        for i in range(n):
            if curSum < 0:
                curSum = 0

            cur = gas[i] - cost[i]
            totalSum += cur
            curSum += cur


            if prev < 0 and cur >= 0:
                ans = i

            prev = curSum

        return ans if totalSum >= 0 else -1



        