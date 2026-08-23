class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)

        for i, val in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                if nums[l] + nums[r] < -val:
                    l += 1
                elif nums[l] + nums[r] > -val:
                    r -= 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l -1]:
                        l += 1

        return res
