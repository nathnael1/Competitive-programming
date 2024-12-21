class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = 0
        count = 0
        prefix = defaultdict(int)
        prefix[0]=1
        for i in range(0,len(nums)):
            if nums[i]%2!=0:
                odd_count += 1
            count += prefix[odd_count-k]
            prefix[odd_count]+=1
        return count