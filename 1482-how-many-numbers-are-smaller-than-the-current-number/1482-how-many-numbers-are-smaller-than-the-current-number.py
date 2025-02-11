from collections import Counter
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #sorting the array
        counter = defaultdict(int)
        sorted_array = sorted(nums)

        #saving the original index for the key of sorted input
        for i in range(len(nums)):
            if sorted_array[i] not in counter:
                counter[sorted_array[i]] = i
        return [counter[num] for num in nums]