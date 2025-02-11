class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        #returning ans[i] = nums[nums[i]]
        ans = [0]  * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans