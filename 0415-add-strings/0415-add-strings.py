import sys
sys.set_int_max_str_digits(10000)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1),len(num2)
        a = 0
        b = 0
        for i in range(l1):
            s = ord(num1[i]) - 48
            a  = a * 10 + s
  
        for i in range(l2):
            s = ord(num2[i]) - 48
            b = b * 10 + s
        return str(a + b)
        