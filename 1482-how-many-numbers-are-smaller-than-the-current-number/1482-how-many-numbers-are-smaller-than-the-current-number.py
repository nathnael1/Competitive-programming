from collections import Counter
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # #using counter for the array
        # count_nums = Counter(nums)
        # res = 0
        # #finding numbers that are greaterrr

        res = []

        #use double iteration to find the value that is less than i
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] >nums[j]:
                    count +=1
            res.append(count)
        
        return res