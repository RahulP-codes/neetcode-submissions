class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0]*26
        for t in tasks:
            freq[ord(t)-ord("A")] += 1

        maxHeap = [-x for x in freq if x != 0]

        heapq.heapify(maxHeap)

        count = 0
        addTask = deque([])

        while maxHeap or addTask:
            count += 1
            print(maxHeap, count)
            newTask = addTask.popleft() if addTask else 0

            if newTask != 0:
                heapq.heappush(maxHeap, newTask)
            
            a = heapq.heappop(maxHeap) if maxHeap else 0

            if a < -1:
                while len(addTask) < n:
                    addTask.append(0)

                addTask.append(a+1)

        return count