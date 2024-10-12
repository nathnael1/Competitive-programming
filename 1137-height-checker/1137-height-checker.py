class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = 0
        newHeights = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != newHeights[i]:
                counter+=1
        return counter