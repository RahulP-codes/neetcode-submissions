class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []

        for x, y in points:
            dist.append(math.sqrt(x**2+y**2))

        sort_this = sorted(zip(dist, points))

        res = [x for _, x in sort_this]

        return res[:k]