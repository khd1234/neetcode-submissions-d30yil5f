class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        res = 0
        l = r = 0
        while r < len(s):
            if s[r] in store:
                l = max(l, store[s[r]] + 1)

            store[s[r]] = r
            res = max(res, r - l + 1) 
            r += 1
        return res
        