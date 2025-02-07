class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        #creating dict to store the product as a key and repetion as value
        my_dict = defaultdict(int)
        
        #itterating through nums
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                my_dict[nums[i] * nums[j]] +=1
        
        res = 0
        #finding the frequency if it matches to 
        for key,value in my_dict.items():
            res += (value-1)*(value)// 2
        return res * 8