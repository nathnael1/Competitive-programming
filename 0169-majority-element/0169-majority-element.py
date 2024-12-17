class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        value = max(counter.values())
        for key,val in counter.items():
            if val == value:
                return key
        