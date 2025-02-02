class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #sorting the array
        nums.sort() 
        #intializing left pointer and total value, and the res value
        left = total = res = 0
        #going through the list by intiallizing the right pointer
        for right in range(len(nums)):
            total+=nums[right]   
            #checking in order to widen the window by using the formula
            #nums[r]* (r - l + 1) > total+k
            while nums[right] * (right - left + 1) > total + k:
                total-=nums[left]
                left+=1
            res = max(res,right - left + 1)
            right+=1

        return res
