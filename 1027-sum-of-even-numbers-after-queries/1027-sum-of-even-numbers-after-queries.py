class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        #res to store each element 
        res = []

        #summing all even creating it
        sum_of_even_numbers = 0
        for num in nums:
            if num % 2 == 0:
                sum_of_even_numbers += num

        #going through each index and value 
        for value,index in queries:
            #if the nums[i] + value is even we substract the nums index  else  we add only the value
            if nums[index] % 2 == 0:
                sum_of_even_numbers-=nums[index]
            nums[index] += value
            if nums[index] % 2 == 0:
                sum_of_even_numbers += nums[index]
            res.append(sum_of_even_numbers)

        return res