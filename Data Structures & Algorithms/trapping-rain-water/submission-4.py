class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]
        drop = 0
        while l < r:
            if max_l <= max_r:
                l += 1
                x = max_l - height[l]
                result = x if x > 0 else 0
                drop += result
                max_l = max(max_l, height[l])
            else:
                r -= 1
                x = max_r - height[r]
                result = x if x > 0 else 0
                drop += result
                max_r = max(max_r, height[r])
        return drop





        