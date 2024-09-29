class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = '1'
        for _ in range(1,n):
            res = []
            counter = 1
            for i in range(1, len(prev)):
                if prev[i] == prev[i-1]:
                    counter+=1
                else:
                    res.append(f'{counter}{prev[i-1]}')
                    counter = 1
            res.append(f'{counter}{prev[-1]}')
            prev = ''.join(res)
        return prev
