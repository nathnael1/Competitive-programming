class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        for i in digits:
            res.append(str(i))
        res = int("".join(res)) + 1
        return [int(i) for i in str(res)]
        