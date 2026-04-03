class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longestSequence = 0
        for i in setNums:
            if i - 1 not in setNums:
                length = 1
                while i + length in setNums:
                    length += 1
                if length > longestSequence:
                    longestSequence = length
        return longestSequence

