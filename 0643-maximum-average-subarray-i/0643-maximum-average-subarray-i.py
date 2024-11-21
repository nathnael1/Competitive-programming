class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        l = 0
        window = sum(nums[:k])
        res = window/k
        for r in range(k,n):
            window+=nums[r]
            window-=nums[l]
            res = max(res,window/k)
            
            l+=1
        return res

