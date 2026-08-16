class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0
        for val in num_set:
            if val - 1 not in num_set:
                length = 1
                while val + length in num_set:
                    length += 1
                result = max(result, length)
        return result