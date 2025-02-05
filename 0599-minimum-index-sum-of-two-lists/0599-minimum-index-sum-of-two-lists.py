class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        #creating one hash table for the first list and caluating the min index for second
        index_counter = {}
        min_sum = float('inf')
        for index in range(len(list1)): 
            index_counter[list1[index]] = index

        #appending to our res key for the minimum index
        res = []
        for index in range(len(list2)):
            if list2[index] in index_counter:
                curr_sum = index_counter[list2[index]] + index
                if curr_sum < min_sum:
                    res = []
                    res.append(list2[index])
                    min_sum = curr_sum
                elif curr_sum == min_sum:
                    res.append(list2[index])

        #returning the result
        return res
            