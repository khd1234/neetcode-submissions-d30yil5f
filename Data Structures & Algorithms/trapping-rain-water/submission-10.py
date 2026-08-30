class Solution:
    def trap(self, height: List[int]) -> int:
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
            
            
                
