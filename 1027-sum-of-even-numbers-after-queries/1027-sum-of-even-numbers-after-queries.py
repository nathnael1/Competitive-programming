class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        #res to store each element 
        res = []

        #summing all the hash_values aftre creating it
        hash_nums = {}
        sum_of_even_numbers = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                hash_nums[i] = nums[i]
                sum_of_even_numbers+=nums[i]

        for val,index in queries:
            nums[index]+=val
            if index in hash_nums:
                if nums[index] % 2 != 0:
                    sum_of_even_numbers -= hash_nums[index]
                    hash_nums.pop(index)
                else:
                    hash_nums[index]+=val
                    sum_of_even_numbers+=val
            else:
                if nums[index] %2 ==  0:
                    hash_nums[index] = nums[index]
                    sum_of_even_numbers += nums[index]
            res.append(sum_of_even_numbers)
        return res