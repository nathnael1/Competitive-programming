class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        value = score[:]
        hash = {}
        value.sort(reverse = True)
        for i in range(len(value)):
            if i + 1 == 1:
                hash[value[i]] = "Gold Medal"
            elif i + 1 == 2:
                hash[value[i]] = "Silver Medal"
            elif i + 1 == 3:
                hash[value[i]] = "Bronze Medal"
            else:
                hash[value[i]] = str(i+1)
        for i in range(len(score)):
            score[i] = hash[score[i]]
        return score


