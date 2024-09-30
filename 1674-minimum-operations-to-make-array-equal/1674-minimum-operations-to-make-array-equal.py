class Solution:
    def minOperations(self, n: int) -> int:
        median = n
        operations = 0
        for i in range(n//2):
            operations += median - ((2 * i) + 1)
        return operations
