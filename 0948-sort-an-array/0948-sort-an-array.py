class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #using merge sort

        #main function
        def merge_sort(nums):
            merge_sort2(nums,0,len(nums)-1)
        
        #merge sort2 function to divide all the items
        def merge_sort2(nums,start,end):
            if start < end:
                middle = (start+end)//2
                merge_sort2(nums,start,middle)
                merge_sort2(nums,middle+1,end)
                merge(nums,start,middle,end)

        #merging all sub part
        def merge(nums,start,middle,end):
            left = nums[start:middle+1]
            right = nums[middle+1:end+1]
            left.append(float("inf"))
            right.append(float("inf"))
            i = j = 0
            for k  in range(start,end+1):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i+=1
                else:
                    nums[k] = right[j]
                    j+=1
        merge_sort(nums)
        return nums