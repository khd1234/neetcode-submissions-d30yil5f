class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in points:
            a, b = i
            dist = -(a*a + b*b)
            if len(heap) < k:
                heapq.heappush(heap, (dist, i))  
            elif dist > heap[0][0]:
                heapq.heappop(heap)    
                heapq.heappush(heap, (dist, i))    

        result = []
        for i in heap:
            result.append(i[1])
        return result
        

        