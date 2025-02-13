class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #sorting the array
        nums.sort()
        res = float('inf')
        #leaving 2 items for last
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            nums1 = nums[i]
            while left < right:
                nums2 = nums[left]
                nums3 = nums[right]
                value = nums1 + nums2 + nums3
                if  value > target:
                    right -=1
                elif value < target:
                    left +=1
                else:
                    return value
                if abs(target - value) < abs(target-res):
                    res = value
        return res
        
                