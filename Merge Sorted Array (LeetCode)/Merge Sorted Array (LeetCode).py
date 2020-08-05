class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cut = len(nums1) - n
        len_nums1 = len(nums1)
        k=cut
        for i in range(n):
            update_element = nums2[i]
            nums1[k]=update_element
            k+=1
        nums1.sort()