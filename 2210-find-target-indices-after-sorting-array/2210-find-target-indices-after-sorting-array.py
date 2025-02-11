class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums.sort()
        #itterating the loop
        for i in range(len(nums)):
            #comparing nums[i] == target and appending the indice in res
                if nums[i] == target:
                    res.append(i)
        return res
