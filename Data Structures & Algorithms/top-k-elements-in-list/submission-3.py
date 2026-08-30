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
        for i in range(n, 0, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res