class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #defining res where 0 is the loser list while 1 is winner
        res = {0:set(),1:set()}
        #going through each winner and loser and if a loser is found appending it in 0 and removing it on 1
        #if a winner is found first checking it is found on 0 if it is skipping else adding it
        more_than_one_lose = []
        for winner, loser in matches:
            res[1].discard(loser)
            if loser in res[0]:
                more_than_one_lose.append(loser)
            res[0].add(loser)
            if winner not in res[0]:
                res[1].add(winner)
        for more_lose in more_than_one_lose:
            res[0].discard(more_lose)

        winner = sorted(res[1])
        losers = sorted(res[0])
        return [winner,losers]
        