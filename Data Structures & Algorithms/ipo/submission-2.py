class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cappro = deque(sorted(zip(capital, profits)))

        project = []

        while k > 0:
            while cappro and cappro[0][0] <= w:
                heapq.heappush(project, -cappro.popleft()[1])

            if not project:
                break

            profit = -heapq.heappop(project)
            w += profit
            k -= 1

        return w