class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for a,b in points:
            value = a**2 + b**2
            distance.append([value,(a,b)])
        distance.sort(key = lambda item: item[0])
        return [b for a,b in distance[:k]]