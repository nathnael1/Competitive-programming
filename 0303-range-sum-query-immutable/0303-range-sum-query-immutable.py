class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0] * (len(nums) + 1 )
        # -2 -2 1 -4  -2 -3
        for i in range(len(nums)):
            self.nums[i + 1] = self.nums[i] + nums[i]


    def sumRange(self, left: int, right: int) -> int:
        value =  self.nums[right+1] - self.nums[left]
        return value


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)