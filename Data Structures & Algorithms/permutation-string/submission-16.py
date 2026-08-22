class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        store = {}
        for i in s1:
            store[i] = store.get(i, 0) + 1

        count = {}
        l = 0
        for r in range(len(s2)):
            count[s2[r]] = count.get(s2[r], 0) + 1
            if r > len(s1) - 1:
                count[s2[l]] -= 1
                if count[s2[l]] == 0:
                    del(count[s2[l]])
                l += 1
            print(store, count)
            if count == store:
                return True
        return False
            
