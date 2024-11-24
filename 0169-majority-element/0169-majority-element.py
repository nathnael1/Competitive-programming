class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for item in nums:
            if count == 0:
                candidate = item
            count += (1 if candidate == item else -1)
        return candidate