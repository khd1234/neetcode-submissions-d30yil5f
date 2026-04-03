class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        max_length = 0
        l = r = 0
        while r < len(s):
            if s[r] not in store:
                store.add(s[r])
                max_length = max(max_length, r - l + 1)
                r += 1
            else:
                store.remove(s[l])
                l += 1
        return max_length
        