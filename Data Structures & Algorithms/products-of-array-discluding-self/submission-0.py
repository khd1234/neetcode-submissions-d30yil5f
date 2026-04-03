class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod, count, index = 1, 0, None
        for i, num in enumerate(nums):
            if num != 0:
                total_prod *= num
            else:
                index = i
                count += 1
        if count > 1:
            return [0] * len(nums)
        elif count == 1:
            res = [0] * len(nums)
            res[index] = total_prod
            return res
        print(total_prod)
        result = []
        for num in nums:
            if num != 0:
                result.append(int(total_prod / num))
            else:
                result.append(total_prod)
        return result

        