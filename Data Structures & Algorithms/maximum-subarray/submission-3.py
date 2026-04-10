class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = result = nums[0]
        if len(nums) == 1:
            return result
        for i in nums[1:]:
            sum += i
            if i > sum:
                sum = i
            if sum > result:
                result = sum
        return result


            

        