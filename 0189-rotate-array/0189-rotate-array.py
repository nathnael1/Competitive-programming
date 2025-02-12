class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k =  k % len(nums)
        left = nums[:-k]
        right = nums[-k:]
        rp  = 0
        lp = 0
        for i in range(len(nums)):
            if rp < len(right):
                nums[i] = right[rp]
                rp+=1
                continue
            if lp < len(left):
                nums[i] = left[lp]
                lp+=1
        