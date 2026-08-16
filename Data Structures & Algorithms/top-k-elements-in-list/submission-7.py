class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for key, val in count.items():
            freq[val].append(key)

        result = []
        for item in freq[::-1]:
            if item:
                for i in item:
                    result.append(i)
                    if len(result) == k:
                        return result
