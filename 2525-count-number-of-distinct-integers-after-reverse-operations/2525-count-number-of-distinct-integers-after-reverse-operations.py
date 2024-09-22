class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            value = int(str(nums[i])[::-1])
            nums.append(value)
        return len(set(nums))