from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #using running - k in dict formula
        nums_counter = defaultdict(int)
        nums_counter[0] = 1
        curr_sum = 0
        res = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            diff = curr_sum - goal
            if diff in nums_counter:
                res += nums_counter[diff]
            nums_counter[curr_sum]+=1
        return res