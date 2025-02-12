from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #counting the frequency
        counter = Counter(s)

        res = []
        pointer = 0
        temp_value = []
        #we must have  0 value for each dictionary
        for i in range(len(s)):
            if counter[s[i]] == 1:
                counter.pop(s[i])
            else:
                counter[s[i]]-=1
            temp_value.append(s[i])
            found = False
            for c in set("".join(temp_value)):
                if counter[c]!=0:
                    found = True
                    break
            if not found:
                res.append(len(temp_value))
                temp_value = []
        return res
                