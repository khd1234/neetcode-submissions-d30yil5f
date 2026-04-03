class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        l = r = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            print(count)
            max_key = max(count.values())
            if (r - l + 1) - max_key <= k:
                max_length = max(max_length, r - l + 1)    
            else:
                count[s[l]] = count.get(s[l]) - 1
                l += 1
            r += 1
        return max_length


        