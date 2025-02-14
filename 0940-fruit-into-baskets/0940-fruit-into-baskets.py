class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #2 baskets
        basket = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(fruits)):
            while len(basket.keys()) == 2 and fruits[r] not in basket:
                basket[fruits[l]]-=1
                if basket[fruits[l]] == 0:
                    basket.pop(fruits[l])
                l+=1
            basket[fruits[r]]+=1
            res = max(res,r-l+1)
        return res

