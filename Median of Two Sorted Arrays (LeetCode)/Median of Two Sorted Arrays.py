class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1 + nums2
        merge.sort()

        merge_len = len(merge)

        def oddeven(merge_len):
            if (merge_len % 2 == 0):
                return True

        def median(list: merge):
            merge_len = len(merge)
            answer = 0.0

            if (oddeven(merge_len)):
                mid = int(merge_len / 2)
                answer = (merge[mid-1] + merge[mid ]) / 2

            else:
                mid = int(merge_len / 2)
                answer = float(merge[mid])

            return answer
        
        output = median(merge)
        return output