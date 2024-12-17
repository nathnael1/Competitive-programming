class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashed = Counter(magazine)
        for c in ransomNote:
            if c in hashed and hashed[c]!=0:
                hashed[c]-=1
                continue
            return False
        return True


