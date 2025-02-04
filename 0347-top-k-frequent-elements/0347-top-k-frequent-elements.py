class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #setting up a counter
        count = Counter(nums)
        #changing a counter to list
        res = [[key,value] for key, value in count.items()]
        #sorting the list res by reverse order 
        res.sort(key = lambda x: x[1], reverse = True)
        #printing the first k elements
        return [item for item,value in res[:k]]