class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        res = 0
        while i < j:
            value = nums[i] + nums[j]
            res = max(res,value)
            i+=1
            j-=1
        return res
