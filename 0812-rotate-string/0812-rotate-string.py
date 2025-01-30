class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        relation = s
        for i in range(len(s)):
            temp = relation  
            relation = temp[1:]
            relation += temp[0]
            if relation == goal:
                return True
        return False