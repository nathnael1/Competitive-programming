class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        #sorting the task in order
        tasks.sort()
        #sorting the processor Time
        processorTime.sort(reverse = True)
        
        j = 0
        res = []
        max_value = float('-inf')
        for i in range(len(tasks)):
            if (i + 1) % 4 != 0:
                value = processorTime[j] + tasks[i]
                max_value = max(value,max_value)
            else:
                value = processorTime[j] + tasks[i]
                max_value = max(value,max_value)
                res.append(max_value)
                max_value = float('-inf')
                j+=1
        return max(res)
