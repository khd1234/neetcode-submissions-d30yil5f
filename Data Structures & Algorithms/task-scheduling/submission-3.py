class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for i in tasks:
            count[i] = count.get(i, 0) + 1
        
        maxHeap = []
        for i in count.values():
            maxHeap.append(-i)
        
        heapq.heapify(maxHeap)
        # print(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            print("time: ", time)
            if maxHeap:
                val = heapq.heappop(maxHeap) + 1
                if val != 0:
                    q.append((time + n, val))
            
            if q and q[0][0] == time:
                heapq.heappush(maxHeap, q[0][1])
                q.popleft()
            print("maxHeap: ", maxHeap)
        return time
            
            


        
        