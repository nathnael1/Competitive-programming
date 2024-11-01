class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        numberOne = 0
        numberTwo = 0
        for i in range(len(num1)):
            numberOne *= 10
            numberOne += ord(num1[i]) - ord("0")
        for j in range(len(num2)):
            numberTwo *= 10
            numberTwo += ord(num2[j]) - ord("0")
        return str(numberOne * numberTwo)
    
      