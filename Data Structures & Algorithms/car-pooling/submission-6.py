class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t:t[1])
        drop = []

        filled = 0
        for np, inp, outp in trips:
            while drop and drop[0][0] <= inp:
                filled -= drop[0][1]
                heapq.heappop(drop)

            filled += np
            heapq.heappush(drop, (outp, np))

            if filled > capacity:
                return False

        return True
        