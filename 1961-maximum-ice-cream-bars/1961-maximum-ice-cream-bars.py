class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        modified_array = [0] * (max(costs) + 1)
        output_array = [0] * len(costs)
        for i in range(len(costs)):
            modified_array[costs[i]] +=1
        for i in range(1,len(modified_array)):
            modified_array[i] += modified_array[i-1]
        for i in costs[::-1]:
            value = modified_array[i] -1
            modified_array[i]-=1
            output_array[value] = i 
        icecream = 0
        total = 0
        for i in output_array:
            total += i
            if total <= coins:
                icecream+=1
            else:
                break
        return icecream