class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        sum = 0

        l = 0
        for i, num in enumerate(nums):
            sum += num
            res = max(res, sum)
            if sum < 0:
                sum = 0
        return int(res)
            
