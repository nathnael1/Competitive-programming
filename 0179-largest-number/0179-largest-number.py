class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #changing each value to string
        for index,value in enumerate(nums):
            nums[index] = str(value)
        
        #constructing comparing funcction
        def compare(n1,n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        res = sorted(nums,key = cmp_to_key(compare))
        return str(int("".join(res) ))
