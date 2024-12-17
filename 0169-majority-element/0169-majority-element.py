class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        majority_key , majority_val = None, 0
        for key,val in counter.items():
            if val > majority_val:
                majority_key,majority_val = key,val
        return majority_key
        