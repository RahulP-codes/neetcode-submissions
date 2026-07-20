class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0

        bestBuy = prices[0]
        for p in prices:
            bestBuy = min(bestBuy, p)

            bestProfit = max(bestProfit, p-bestBuy)

        return bestProfit
        