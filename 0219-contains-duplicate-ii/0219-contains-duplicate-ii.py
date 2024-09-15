class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}
        for i,value in enumerate(nums):
            if value in hash and abs(hash[value]-i) <= k:
                return True
            hash[value] = i
        return False
        
                