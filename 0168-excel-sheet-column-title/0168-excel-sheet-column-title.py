class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #this question is same concept with 10 base but since we have 26 character it is base 16

        #creating res variable to store the output
        res = []
        #itterating column number until it is 0 
        while columnNumber > 0: 
            #we have to substact one( since it is 0 indexed) and  we have to add the value of A
            exact_value = columnNumber - 1
            character_value = chr(ord('A') + (exact_value % 26))
            print(character_value)
            #appending it to our res
            res.append(character_value)
            #dividing and reducing column-1 by 26
            columnNumber = (columnNumber-1)//26
        return "".join(res[::-1])