class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #sorting using 2 pointer approach 
        #paring thin person with fat one
        people.sort()
        l = 0
        r = len(people) - 1
        boat = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l+=1
            boat+=1
            r-=1
        return boat
        