class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        #To change the number to round number first we check if the number is greater than the first item
        #on the val, if it is we append it to our arary and decrease our number by the value then
        # if not we will do nothing

        i = 0
        res = []
        for value,roman in  val:
            if num == 0:
                break
            count = num//value
            res.append(count*roman)
            num -= count * value
        return "".join(res)

