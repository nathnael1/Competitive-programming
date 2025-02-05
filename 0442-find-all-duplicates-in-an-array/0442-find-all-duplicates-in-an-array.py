class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #creating a counter
        counter_nums = Counter(nums)
        res = []
        #appending to our res of all values that are found more than one
        for key,value in counter_nums.items():
            if value > 1:
                res.append(key)
        return res