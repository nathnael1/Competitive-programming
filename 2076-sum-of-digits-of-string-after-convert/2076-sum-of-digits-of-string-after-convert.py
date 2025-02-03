class Solution:
    def getLucky(self, s: str, k: int) -> int:
        #hahsing all integers from a to z
        letter_to_number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 
        'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 
        'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        #creating a list that store the value of the number of hashed string
        number_holder = []
        for i in range(len(s)):
            number_holder.append(str(letter_to_number[s[i]]))
        number_holder = list("".join(number_holder))
        #summing the list k operation
        for i in range(k):
            res = sum([int(x) for x in number_holder])
            number_holder = [int(x) for x in str(res)]
        return res