class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        #soring the element using lambda with key of k
        score.sort(key = lambda x : x[k],reverse = True)
        return score