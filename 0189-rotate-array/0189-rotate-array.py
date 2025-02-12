class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_index(start,end):
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start+=1
                end-=1
        k = k % len(nums)
        nums.reverse()
        reverse_index(0,k-1)
        reverse_index(k,len(nums)-1)

