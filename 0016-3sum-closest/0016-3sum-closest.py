class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(0,len(nums)-2):
            j, k = i+1,len(nums)-1
            while j < k:
                value = nums[i] + nums[j] + nums[k]
                if abs(value-target) < abs(res - target):
                    res = value
                if value > target:
                    k-=1
                elif value < target:
                    j+=1
                else: 
                    return value
        return res
