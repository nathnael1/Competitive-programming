class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        for i in range(1,len(score)):
            for j in range(i-1,-1,-1):
                valuebefore = score[j][k]
                valueafter =  score[j+1][k]
                if valuebefore < valueafter:
                    score[j],score[j+1] = score[j+1],score[j]
                else:
                    break
        return score
        

