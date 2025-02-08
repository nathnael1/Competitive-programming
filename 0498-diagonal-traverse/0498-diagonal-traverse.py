from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        #output array
        res = []

        #using dictionary to append when diagonal sum is equal 
        neg_diagonal = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                neg_diagonal[i+j].append(mat[i][j])

        #returning in the desired format

        top = True
        for value in neg_diagonal.values():
            if top == True:
                value.reverse()
                for item in value:
                    res.append(item)
                top = False
            else:
                for item in value:
                    res.append(item)
                top = True
        return res

