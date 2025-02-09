from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        #counting each value 
        answers_count = Counter(answers)
        res = 0
        for key,value in answers_count.items():
            number = ((value - 1)//(key+1))+1
            res += number*(key+1)

        return res

 
