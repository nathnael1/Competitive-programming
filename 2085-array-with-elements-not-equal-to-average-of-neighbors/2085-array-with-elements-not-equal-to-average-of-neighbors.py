class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        l,r = 0,(len(nums)//2)+1
        while len(res)!=len(nums):
            if l <=  len(nums)//2:
                res.append(nums[l])
                l+=1
            if r < len(nums):
                res.append(nums[r])
                r+=1
        return res