class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        counter = 0
        check = True
        while  check:
            for i in range(len(tickets)):

                if tickets[i] > 0:
                    counter+=1
                    tickets[i]-=1
                if i == k and tickets[k] == 0:
                    check = False
                    break
        return counter
                    