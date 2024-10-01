class Solution:
    def stringHash(self, s: str, k: int) -> str:
        
        times = len(s)//k
        result = [""]* times
        prev = 0
        for i in range(times):
            temp = s[prev:k + prev]
            counter = 0
            for char in temp:
                counter+= ord(char) - 97
            counter %= 26 
            result[i] = chr(counter+97)
            prev+= k
        return "".join(result)