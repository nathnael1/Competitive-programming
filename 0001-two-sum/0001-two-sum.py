class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed = {}
        for i in range(len(nums)):
            if nums[i] not in hashed:
                hashed[target-nums[i]] = i
                continue
            return [hashed[nums[i]],i]