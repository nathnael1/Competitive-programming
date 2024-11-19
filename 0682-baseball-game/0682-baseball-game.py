class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for item in operations:
            if item == "D":
                res.append(res[-1] * 2)
            elif item == "C":
                res.pop()
            elif item == "+":
                res.append(res[-1] + res[-2])
            else:
                res.append(int(item))
        return sum(res)