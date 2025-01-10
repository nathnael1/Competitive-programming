class Solution:
    def minTimeToType(self, word: str) -> int:
        pointer = 'a'
        counter = 0
        l = 0
        while l < len(word):
            target = ord(word[l])
            current = ord(pointer)
            clockwise = abs(target-current)
            counter_clockwise= 26 - clockwise
            counter += min(clockwise,counter_clockwise) + 1
            pointer = word[l]
            l+=1
        return counter