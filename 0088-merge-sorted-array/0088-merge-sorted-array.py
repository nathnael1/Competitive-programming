class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_pointer = m-1
        nums2_pointer = n-1
        last = m+n-1
        while nums1_pointer >= 0 and nums2_pointer >= 0:
            if nums1[nums1_pointer] > nums2[nums2_pointer]:
                nums1[last] = nums1[nums1_pointer]
                nums1_pointer-=1
            else:
                nums1[last] = nums2[nums2_pointer]
                nums2_pointer-=1
            last-=1
        while nums2_pointer >= 0:
            nums1[last] = nums2[nums2_pointer]
            nums2_pointer-=1
            last-=1