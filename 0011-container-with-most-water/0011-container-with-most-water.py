class Solution:
    def maxArea(self, height: List[int]) -> int:
        #using 2 pointer approach
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            #calculating the maximum at each iteration
            h = min(height[r],height[l])
            #using height as an indicator
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
            width = r-l+1

            area = max(area,width*h)

        return area 

