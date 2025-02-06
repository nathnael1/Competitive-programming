class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        #intializing the remove all elements and the sum of all elements
        all_element_sum = (n * (n+1) ) // 2
        removed_all_elements = set()

        #intializing count as 1 for starting point
        counter = 0
        i = 1
        while i <= n:
            counter+=1
            if n-1 == len(removed_all_elements):
                break

            if counter == k and i not in removed_all_elements:
                removed_all_elements.add(i)
                counter = 0
            elif i in removed_all_elements:
                counter -= 1 

            #creating circular list
            if i == n:
                i = 0
                 
            i+=1  

        #returning the winner
        return all_element_sum - sum(removed_all_elements)