class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if not word:
            return ""
        prefix = ""
        holder = word
        not_found = True
        for c in word:
            prefix+=c
            holder = holder[1:]
            if c == ch:
                not_found = False
                return prefix[::-1] + holder
        if not_found:
            return word