class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #we have to find the conter
        majority_number = len(nums)//2
        count = Counter(nums)
        #and return the value if we found value > nums
        for key,value in count.items():
            if value > majority_number:
                return key