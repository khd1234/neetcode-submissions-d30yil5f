class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        store = {}
        res = 0
        l = r = 0
        while r < len(s):
            if s[r] in store:
                l = max(store[s[r]] + 1, l)

            res = max(res, r - l)
            store[s[r]] = r
            r += 1
        return res + 1
        