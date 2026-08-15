class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = [0] * 26;
        for i in s:
            count_s[ord(i) - ord('a')] += 1

        count_t = [0] * 26;
        for i in t:
            count_t[ord(i) - ord('a')] += 1
        
        for i in range(26):
            if count_s[i] != count_t[i]:
                return False
        return True
        