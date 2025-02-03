class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        #saving all left and right range in original set
        my_set=set()
        for start,end in ranges:
            for i in range(start,end+1):
                my_set.add(i)
        for j in range(left,right+1):
            if j not in my_set:
                return False
        return True
        #going through each loop
