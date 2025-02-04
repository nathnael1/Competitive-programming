from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        #itterating through the list
        for item in paths:
            directory,*file_name = item.split()
            for unique_file in file_name:
                start = unique_file.find("(") +1
                end = unique_file.find(")") 
                content = unique_file[start:end]
                file_type = unique_file[:start-1]
                name = directory+"/"+file_type
                my_dict[content].append(name)
        res = []
        for item,value in my_dict.items():
            if len(value) > 1:
                res.append(value)
        return res

                