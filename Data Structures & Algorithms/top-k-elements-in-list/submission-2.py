class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for i in range(n+1)]
        for key, value in count.items():
            freq[value].append(key)

        res = []
        cnt = 0
        for i in range(n, 0, -1):
            if cnt >= k:
                break
            if freq[i]:
                res.extend(freq[i])
                cnt += len(freq[i])

        return res
        
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        return [sorted_count[i][0] for i in range(k)]