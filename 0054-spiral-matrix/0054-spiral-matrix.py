class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_length = len(matrix)
        col_length = len(matrix[0])
        all_element_length = row_length * col_length

        #creating directions used for toggling
        right,bottom,up,left = 0,1,2,3
        direction = right
        
        #creating bound for left right bottom and top wall
        up_wall = 0
        left_wall = -1
        right_wall = col_length
        bottom_wall = row_length
        i =  j = 0
        res = []

        while len(res) < all_element_length:
            if direction == right:
                while j < right_wall:
                    res.append(matrix[i][j])
                    j+=1
                i+=1
                j-=1 #since j is out of bound
                direction = bottom
                right_wall -= 1  
            elif direction == bottom:
                while i < bottom_wall:
                    res.append(matrix[i][j])
                    i+=1
                i-=1
                j-=1 #since j is out of bound
                direction = left
                bottom_wall -= 1
            elif direction == left:
                while j > left_wall:
                    res.append(matrix[i][j])
                    j-=1
                i-=1
                j+=1 #since j is out of bound
                direction = up
                left_wall +=1

            elif direction == up:
                while i > up_wall:
                    res.append(matrix[i][j])
                    i-=1
                i+=1
                j+=1 
                direction = right
                up_wall +=1
        return res