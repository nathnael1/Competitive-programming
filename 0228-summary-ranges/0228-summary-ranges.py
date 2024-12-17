class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] !=1:
                if nums[i-1]!=start:
                    res.append(f"{start}->{nums[i-1]}")
                else:
                    res.append(f"{start}")
                start = nums[i]
        if start!=nums[-1]:
            res.append(f"{start}->{nums[-1]}")
        else:
            res.append(f"{nums[-1]}")
        return res