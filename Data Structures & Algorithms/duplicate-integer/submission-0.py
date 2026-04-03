class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i in nums:
            if my_dict.get(i, False):
                return True
            my_dict[i] = True

        return False
        
         