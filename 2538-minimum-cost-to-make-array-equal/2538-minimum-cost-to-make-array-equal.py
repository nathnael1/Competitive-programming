class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        #zipping it togather and sorting it based on nums
        cont = list(zip(nums,cost))
        cont.sort(key = lambda x: x[0])

        #constructing prefix
        prefix = [0] * len(cont)
        curr_cost = cont[0][1]
        prefix_sum = 0
        for i in range(1,len(cont)):
            diff = cont[i][0] - cont[i-1][0]
            prefix[i] = ((curr_cost) * diff) + prefix_sum
            prefix_sum = prefix[i]
            curr_cost += cont[i][1]

        #constructing suffix at res1
        curr_cost = cont[-1][1]
        prefix_sum = 0
        suffix = [0]*len(nums)
        for i in range(len(cont)-2,-1,-1):
            diff = abs(cont[i][0] - cont[i+1][0])
            suffix[i] = ((curr_cost) * diff) + prefix_sum
            prefix_sum = suffix[i]
            curr_cost += cont[i][1]
        
        #adding res value
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] + suffix[i]
        return min(res)
        
            