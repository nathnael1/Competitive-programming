class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashed = defaultdict(int)
        for item in nums:
            hashed[item]+=1
        value = max(hashed,key = hashed.get)
        return value