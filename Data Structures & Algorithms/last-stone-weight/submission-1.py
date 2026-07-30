class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nstones = [-x for x in stones]

        heapq.heapify(nstones)

        while len(nstones) > 1:
            x, y = heapq.heappop(nstones), heapq.heappop(nstones)

            if x == y:
                continue
            else:
                heapq.heappush(nstones, x-y)
                
        return -nstones[0] if nstones else 0