class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            a, b = heapq.heappop(heap), heapq.heappop(heap)
            if a < b:
                heapq.heappush(heap, a - b)
            print(heap)
        if heap:
            if heap[0] < 0:
                return -heap[0]
            return heap[0]
        return 0