from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        number_of_left_over = 0
        number_of_pairs = 0

        #hashing each value
        hashed_value = Counter(nums)

        #number of pair is n//2 while number of left over is n % 2
        for value in hashed_value.values():
            number_of_pairs += value //2
            number_of_left_over += value % 2
        return [number_of_pairs,number_of_left_over]


