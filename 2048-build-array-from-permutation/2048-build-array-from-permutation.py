class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        #returning we have to use meta = a+ b*1001
        #where a = nums[i] and b = nums[nums[i]]
        
        const_n = 1001
        for i in range(len(nums)):
            a = nums[i]
            b = nums[a]%const_n
            nums[i] = a + b*const_n
    

        #decrypting meta
        for i in range(len(nums)):
            nums[i]//=const_n

        return nums