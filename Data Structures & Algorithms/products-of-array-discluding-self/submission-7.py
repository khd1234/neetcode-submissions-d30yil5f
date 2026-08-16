class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [nums[0]]
        for i in range(1, len(nums)):
            prods.append(prods[i-1] * nums[i])
        
        result = [1] * len(nums)

        running = 1
        for i in range(len(nums) - 1, 0, -1):
            result[i] = prods[i - 1] * running
            running *= nums[i]
        result[0] = running
        
        return result
        

        

