class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #creating res variable to store the majority element

        res = []

        #finding the majority number 
        majority_number = len(nums)//3
        counter_nums = Counter(nums)
        #check each counter
        for key,value in counter_nums.items():
            if value > majority_number:
                res.append(key)
        return list(set(res))