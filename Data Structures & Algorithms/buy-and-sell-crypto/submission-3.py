class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small = float('inf')
        max_diff = 0
        for i in prices:
            small = min(small, i)
            max_diff = max(max_diff, i - small)
        return max_diff

        