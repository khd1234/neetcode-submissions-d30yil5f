class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] 
        for i in range(1, len(nums)):
            result.append(nums[i-1] * result[i-1])
        running = 1
        for i in range(len(result) - 1, -1, -1):
            result[i] = result[i] * running
            running = running * nums[i]
        return result

            

        