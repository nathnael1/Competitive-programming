class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        numone = 0
        numtwo = 0
        for c in num1:
            value = ord(c) - ord('0')
            numone = (numone*10) +  value
        for c in num2:
            value = ord(c) - ord('0')
            numtwo = (numtwo*10) +  value
        return str(numone*numtwo)
      