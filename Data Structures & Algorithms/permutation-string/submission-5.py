class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        for i in s1:
            count_s1[i] = count_s1.get(i, 0) + 1
        count_s2 = {}
        for i in s2[0: len(s1)]:
            count_s2[i] = count_s2.get(i, 0) + 1
        if count_s1 == count_s2:
            return True
        
        l = 0
        r = len(s1)
        while r < len(s2):            
            count_s2[s2[l]] -= 1
            if count_s2[s2[l]] == 0:
                del count_s2[s2[l]]
            count_s2[s2[r]] = count_s2.get(s2[r], 0) + 1
            if count_s1 == count_s2:
                return True
            l += 1
            r += 1
        return False
        
            


        