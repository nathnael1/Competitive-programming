class Solution:

    def reductionOperations(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        unique_values = sorted(frequency.keys(), reverse = True)
        cumulative = 0
        operation = 0
        for i in range(1,len(unique_values)):
            cumulative += frequency[unique_values[i-1]]
            operation+=cumulative
        return operation
               
                