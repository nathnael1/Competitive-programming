class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        relation = s+s
        if goal in relation:
            return True
        else:
            return False