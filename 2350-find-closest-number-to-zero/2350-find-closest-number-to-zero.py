class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in nums:
            if abs(i) == abs(res):
                res = max(i,res)
            elif abs(i) < abs(res):
                res = i
        return  res