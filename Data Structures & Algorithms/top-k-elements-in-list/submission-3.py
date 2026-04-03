class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        resu = []
        flag = 0
        for i in freq[::-1]:
            if i:
                flag += 1
                for j in i:
                    resu.append(j)
                if len(resu) == k:
                    return resu



        