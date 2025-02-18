class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #running sum 
        res = 0
        storing_dict = defaultdict(int)
        storing_dict[0]=1
        prefix = 0
        for i in range(len(nums)):
            prefix+=nums[i]
            if (prefix - k) in storing_dict:
                res += storing_dict[prefix-k]
            storing_dict[prefix]+=1
        return res

