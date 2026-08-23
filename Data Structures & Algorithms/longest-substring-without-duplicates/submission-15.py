class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        store = {}
        l = 0
        for r in range(len(s)):
            if s[r] in store:
                l = max(l, store[s[r]] + 1)
            store[s[r]] = r
            res = max(res, r - l + 1)
        return res