class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        distri = [1]*n

        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                distri[i] = distri[i-1] + 1
            # else:
            #     distri[i] = distri[i-1]
        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                distri[i] = max(distri[i+1] + 1, distri[i])
            # else:
            #     distri[i] = distri[i+1]

        return sum(distri)

            
            
        