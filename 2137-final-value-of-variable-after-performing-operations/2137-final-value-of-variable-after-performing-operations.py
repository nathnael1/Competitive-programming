class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for opr in operations:
            if opr == "--X" or opr == "X--":
                x-=1
            elif opr == "++X" or opr == "X++":
                x+=1
        return x