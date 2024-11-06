class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashed = {}
        for c in magazine:
            hashed[c] = hashed.get(c,0) + 1
        for c in ransomNote:
            if hashed.get(c,0) ==  0:
                return False
            hashed[c]-=1
        return True

