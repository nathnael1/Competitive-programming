class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_window = sum(nums[:k])
        max_value = current_window
        for number in range(k,len(nums)):
            current_window+=nums[number]-(nums[number-k])
            max_value = max(current_window,max_value)
        return max_value/k