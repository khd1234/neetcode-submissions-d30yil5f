class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        max_diff = 0
        for i in range(len(prices)):
            max_diff = max(max_diff, prices[i] - min_value)
            min_value = min(min_value, prices[i])
        return max_diff
                

        