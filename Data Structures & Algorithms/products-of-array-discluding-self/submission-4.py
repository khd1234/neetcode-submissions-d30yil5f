class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] 
        running = 1
        for i in range(1, len(nums)):
            running *= nums[i - 1]
            result.append(running)

        running = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= running
            running = running * nums[i]
        
        return result
        


            

        