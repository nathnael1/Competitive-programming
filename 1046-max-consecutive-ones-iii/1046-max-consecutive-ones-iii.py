class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #creating an array
        res = defaultdict(int)
        max_width = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                while res[nums[right]] >= k:
                    res[nums[left]] -= 1
                    left+=1
            res[nums[right]] += 1
            max_width = max(max_width,right - left +1)
        return max_width

