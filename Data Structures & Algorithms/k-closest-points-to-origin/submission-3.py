class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []

        for x, y in points:
            dist.append(math.sqrt(x**2+y**2))

        sort_this = sorted(zip(dist, points))

        res = [sort_this[i][1] for i in range(k)]

        return res