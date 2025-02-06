class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        #creating duplicated array
        row_length = len(img)
        col_length = len(img[0])
        res_matrix = [[0]*col_length for i in range(row_length)]
        #iterrating through the array
        for row_index in range(len(img)):
            #total_sum and number of items

            for col_index in range(len(img[row_index])):
                total_sum=img[row_index][col_index]
                total_count = 1
                #same column and one row up
                if row_index != 0:
                    #incremening count and adding total_sum
                    total_sum += img[row_index-1][col_index]
                    total_count +=1
                 #same column and one row down
                if row_index != len(img) - 1:
                    #incremening count and adding total_sum
                    total_sum += img[row_index+1][col_index]
                    total_count +=1
                # one row up and one column left
                if row_index != 0 and col_index!=0:
                    #incremening count and adding total_sum
                    total_sum += img[row_index-1][col_index-1]
                    total_count +=1

                # one row up and one column right
                if row_index != 0 and col_index!=len(img[row_index]) - 1:
                    #incremening count and adding total_sum
                    total_sum += img[row_index-1][col_index+1]
                    total_count +=1

                # one row down and one column left
                if row_index != len(img) - 1 and col_index!=0:
                    #incremening count and adding total_sum
                    total_sum += img[row_index+1][col_index-1]
                    total_count +=1

                # same row right column

                if col_index != (len(img[0]) - 1):
                    
                    #incremening count and adding total_sum
                    total_sum += img[row_index][col_index + 1]
                    total_count +=1

                           
                # one row down and one column right
                if row_index != len(img) - 1 and col_index!=len(img[row_index]) - 1:
                    #incremening count and adding total_sum
                    total_sum += img[row_index+1][col_index+1]
                    total_count +=1

                #same row left column
                if col_index != 0:
                    #incremening count and adding total_sum
                    total_sum += img[row_index][col_index-1]
                    total_count +=1
                
                average_value = total_sum//total_count
                res_matrix[row_index][col_index] = average_value
        return res_matrix

                

                

