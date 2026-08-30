class Solution:
    def trap(self, height: List[int]) -> int:

        # max_right = [0] * len(height)
        # max_val = 0
        # for i in range(len(height) - 1, -1, -1):
        #     max_right[i] = max_val
        #     max_val = max(max_val, height[i])

        # result = 0
        # curr_max = 0
        # for i in range(len(height)):
        #     min_height = min(curr_max, max_right[i])
        #     result += max(0, min_height - height[i])
        #     curr_max = max(curr_max, height[i])
        # return result

        result = 0

        l = 0
        r = len(height) - 1
        left_max, right_max = height[l], height[r]
        while l < r:
            if left_max < right_max:
                l += 1
                result += max(0, left_max - height[l])
                left_max = max(left_max, height[l])
            else:
                r -= 1
                result += max(0, right_max - height[r])
                right_max = max(right_max, height[r])
        return result
            
            
                
