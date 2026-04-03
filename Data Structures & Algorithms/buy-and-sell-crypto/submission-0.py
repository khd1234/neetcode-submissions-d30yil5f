class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_array = [0] * len(prices)
        max_element = prices[len(prices) - 1]
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > max_element:
                max_element = prices[i]
            max_array[i] = max_element

        max_diff = 0
        for i in range(len(prices)):
            if max_array[i] - prices[i] > max_diff:
                max_diff = max_array[i] - prices[i]
        return max_diff
                

        