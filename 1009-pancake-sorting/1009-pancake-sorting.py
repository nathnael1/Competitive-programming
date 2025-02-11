from collections import defaultdict
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        #constructing flip
        def flip(end):
            start = 0
            while start < end:
                arr[start],arr[end] = arr[end],arr[start]
                start += 1
                end -= 1
        
        #fliping the maximum to the last index
        for i in range(len(arr)-1,-1,-1):
            max_index = i
            for j in range(i-1,-1,-1):
                if arr[j] > arr[max_index]:
                    max_index = j
            if max_index != i:
                flip(max_index)
                flip(i)
                ans.append(max_index+1)
                ans.append(i+1)
        return ans
            


                


