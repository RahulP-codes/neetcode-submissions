class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        res = []

        t = deque(sorted(zip(tasks, range(0, n))))
        print(t)

        q = []
        enq = t[0][0][0]
        last_enq = t[-1][0][0]
        print(enq)
        print(last_enq)

        while enq <= last_enq:
            print(".", enq)
            while t and enq >= t[0][0][0]:
                print("1.", t[0][0][0])
                (en, p), i = t.popleft()
                heapq.heappush(q, ([p, en], i))
            
            if q:
                (ptime, en), idx = q[0]
                res.append(idx)
                heapq.heappop(q)
                enq = enq + ptime
                print("2.", enq, idx, en)
                continue

            enq = t[0][0][0]
            print("3.", enq)

        while t:
            (en, p), i = t.popleft()
            heapq.heappush(q, ([p, en], i))

        while q:
            (ptime, en), idx = q[0]
            res.append(idx)
            heapq.heappop(q)
        

        return res