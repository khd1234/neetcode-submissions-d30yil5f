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
                val = heapq.heappop(maxHeap)
                if val < -1:
                    q.append((val + 1, time + n))
            
            print(q)
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q[0][0])
                q.popleft()
            print("maxHeap: ", maxHeap)
        return time
            
            


        
        