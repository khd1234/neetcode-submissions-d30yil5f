class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_difference = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                max_difference = max(max_difference, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        return max_difference

        