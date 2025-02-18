from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        table = defaultdict(int)
        table[0] = 1
        #using remainder as key and adding value
        curr_sum = 0
        res = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            res += table[curr_sum%k]
            table[curr_sum%k] +=1
        return res