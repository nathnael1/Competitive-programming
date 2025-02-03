class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        #saving all left and right range in original set
        original_set = {num for num in range(left,right+1)}
        #going through each loop
        for i in range(len(ranges)):
            left_range = ranges[i][0]
            right_range = ranges[i][1]
            #and checking each element exist in a set and if it exist removing it from the original set
            for j in range(left_range,right_range+1):
                if j in original_set:
                    original_set.discard(j)
            if not original_set:
                return True
        return not original_set