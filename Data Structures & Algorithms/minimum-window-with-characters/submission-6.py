class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, countS = {}, {}
        for i in t:
            countT[i] = countT.get(i, 0) + 1
        have = 0
        need = len(countT)
        result = [-1, -1]
        resLen = float("infinity")
        left = 0
        for i in range(len(s)):
            char = s[i]
            countS[char] = countS.get(char, 0) + 1
            if char in countT and countS[char] == countT[char]:
                have += 1
            
            while have == need:
                # if s[left] not in countT:
                #     left += 1
                #     continue
                if i - left + 1 < resLen:
                    resLen = i - left + 1
                    res = [left, i]
                countS[s[left]] -= 1
                if s[left] in countT and countS[s[left]] < countT[s[left]]:
                    have -= 1
                
                left += 1
        if resLen != float("infinity"):
            return s[res[0]: res[1] + 1]
        else:
            return ""




        