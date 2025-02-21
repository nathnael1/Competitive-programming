
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        #prefix sum of range
        prefix = [0]*(len(nums))
        for start,end in requests:
            prefix[start]+=1
            if end + 1 < len(nums):
                prefix[end+1]-=1
        #finding prefix
        for i in range(1,len(nums)):
            prefix[i]+=prefix[i-1]
        
        #sorting the list based on prefix value
        zipped_sorted = []
        for i in range(len(nums)):
            zipped_sorted.append((prefix[i],i))
        zipped_sorted.sort(key = lambda x: x[0],reverse = True)

        #to match the sorting
        nums.sort(reverse = True)
        ordered = [0]*len(nums)
        i = 0
        for rep, index in zipped_sorted:
            ordered[index] = nums[i]
            i+=1
        
        #prefix sum for res
        for i in range(1,len(ordered)):
            ordered[i]+= ordered[i-1]
        
        ans = 0
        for start,end in requests:
            if start == 0:
                ans+=ordered[end]
                continue
            ans+= ordered[end]-ordered[start-1]
        return ans % (10**9 + 7)
        
        