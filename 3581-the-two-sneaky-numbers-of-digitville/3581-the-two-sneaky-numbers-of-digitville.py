class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        #create a counter to get all the values
        counter_nums = Counter(nums)
        #create res which store digits appear more than 1
        res = []
        #store the digit if the value is appeared more than one
        for key,values in counter_nums.items():
            if values > 1:
                res.append(key)
        return res