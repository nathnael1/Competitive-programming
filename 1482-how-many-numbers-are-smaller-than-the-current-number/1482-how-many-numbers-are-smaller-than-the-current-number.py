class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in counter:
                counter[sorted_nums[i]] = i
        return [counter[num] for num in nums]