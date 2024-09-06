class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""] * len(s)

        for index,value in enumerate(indices):
            res[value] = s[index]
        return "".join(res)
            