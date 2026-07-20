class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        ans = []

        for i, a in enumerate(nums):
            if a>0:
                break

            if i>0 and nums[i-1] == a:
                continue

            l, r = i+1, n-1
            while l<r:
                summ = a + nums[l] + nums[r]
                if summ < 0:
                    l += 1
                elif summ > 0:
                    r -= 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1 
                    while nums[l-1] == nums[l] and l<r:
                        l += 1

        return ans