class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        #sorting each array
        seats.sort()
        students.sort()

        #finding the difference for each value
        count = 0
        for i in range(len(seats)):
            count += abs(seats[i] - students[i])
        return count