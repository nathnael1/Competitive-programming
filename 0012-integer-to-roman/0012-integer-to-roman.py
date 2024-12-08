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
        res = ''
        for number,roman in val:
            count = num//number
            res += count * roman
            num-=count * number
        return res
