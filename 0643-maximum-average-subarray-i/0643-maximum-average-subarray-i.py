class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #finding the intial window sum
        window = sum(nums[:k])
        max_average = window/k
        for i in range(len(nums)-k):
            window += nums[i+k]-nums[i]
            max_average = max(max_average,window/k)
        return max_average