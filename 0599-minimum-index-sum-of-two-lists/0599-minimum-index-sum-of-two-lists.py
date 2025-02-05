class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        min_index = float('inf')
        #going through both the loop 
        for i in range(len(list1)):
            for j in range(len(list2)):
                #Calculating sum index
                #we are going to append our item but if the sum index is less than we are going to pop it
                curr_index = i + j
                if list1[i] == list2[j]:
                    if curr_index < min_index:
                        res = []
                        res.append(list1[i])
                        min_index = curr_index
                    elif curr_index == min_index:
                        res.append(list1[i])
        #returning the result
        return res
            