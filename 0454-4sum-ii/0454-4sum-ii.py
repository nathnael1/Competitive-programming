from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter = 0
        sumup = defaultdict(int)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                value = nums1[i] + nums2[j]
                sumup[value] += 1
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                value = nums3[i] + nums4[j]
                if - value in sumup:
                    counter += sumup[-value]
        return counter