class Solution:
    def sortSentence(self, s: str) -> str:
        holder = s.split()
        res = ['']* len(holder)
        ans = ""
        for word in holder:
            index = int(word[-1]) - 1
            res[index] = word
        for i in range(len(res)):
            for j in range(len(res[i])):
                if j == len(res[i]) - 1 and i!= len(res) - 1:
                    ans+= " "
                    continue
                elif j == len(res[i]) - 1:
                    continue
                ans += res[i][j]
                
        return ans
