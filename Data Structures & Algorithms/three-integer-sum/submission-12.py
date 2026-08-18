class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            result.extend(self.twoSum(nums, i))
        return result

    def twoSum(self, nums, i):
        res = []
        l = i + 1
        r = len(nums) - 1
        target = -nums[i]

        while l < r:
            current = nums[l] + nums[r]
            if current < target:
                l += 1
            elif current > target:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1

                # Skip duplicates
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
        return res
        
