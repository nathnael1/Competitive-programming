class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        #creating res variable to store the result
        res = []
        #creating a flag that store is_block or ntot default value of false
        is_block = False
        new_line = []
        #going through each line
        for line in source:
            i = 0
            while i < len(line):
            #checking each character and determining based on conditions of /* */ and //
                if not is_block:
                    if line[i:i+2] == "/*":
                        i+=1
                        is_block = True
                    elif line[i:i+2] == "//":
                        break
                    else:
                        new_line.append(line[i])
                else:
                    if line[i:i+2] == "*/":
                        i+=1
                        is_block = False
                i+=1
            if new_line and not is_block:
                res.append("".join(new_line))
                new_line = []
                
        return res