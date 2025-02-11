class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #using insertion sort
        for i in range(1,len(nums)):
            for j in range(i-1,-1,-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                else:
                    break

        #using buble sort
        # for i in range(len(nums)):
        #     for j in range(len(nums)-1-i):
        #         if nums[j] > nums[j+1]:
        #             nums[j],nums[j+1] = nums[j+1],nums[j]

        # #using selection sort
        # for i in range(len(nums)):
        #     min_index = i
        #     for j in range(i+1,len(nums)):
        #         if nums[j] < nums[min_index]:
        #             min_index = j
        #     if min_index != i:
        #         nums[i],nums[min_index] = nums[min_index], nums[i]